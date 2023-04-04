from django.shortcuts import render
from django.views.generic import TemplateView

from django.utils import timezone
from .models import UploadedFile
from .forms import UploadForm
# Create your views here.
from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
#from langchain.llms import OpenAIChat
from langchain.chat_models import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = ''


class HomePageView(TemplateView):
    template_name = "home_signin/homepage.html"


class AboutUsView(TemplateView):
    template_name = "home_signin/pages/about-us.html"


class AuthorView(TemplateView):
    template_name = "home_signin/pages/author.html"


class ContactUsView(TemplateView):
    template_name = "home_signin/pages/contact-us.html"


class SignInView(TemplateView):
    template_name = "home_signin/pages/sign-in.html"


class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"


class ConvertView(TemplateView):
    template_name = "dashboard/convert.html"

    def post(self, request, *args, **kwargs):
        print(request.FILES['file'])
        print("Call Came here")
        # print(request.POST.get("password"))
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("form Valid")
            uploaded_file = request.FILES['file']
            filename = uploaded_file.name
            print(filename)
            # Write the uploaded file to the server
            with open(filename, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            # Create a new UploadedFile object and save it to the database
            uploaded_file_object = UploadedFile(
                file=filename,
                uploaded_at=timezone.now()
            )
            uploaded_file_object.save()
            print(uploaded_file_object.file.path)
            # Do something with the uploaded file or the database object
            return render(request, 'dashboard/convert.html')
        return render(request, 'dashboard/dashboard.html')

    def list_files(request, *args, **kwargs):
        print("inside list files")
        uploaded_files = UploadedFile.objects.all()
        return render(request, "dashboard/convert.html", {"uploaded_files": uploaded_files})

    def construct_index(directory_path):
        max_input_size = 4096
        num_outputs = 512
        max_chunk_overlap = 20
        chunk_size_limit = 600

        prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

        # llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))
        llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo"))
        documents = SimpleDirectoryReader(directory_path).load_data()
        print(len(documents))
        index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

        index.save_to_disk('index.json')

        return index

    def process_files(request, *args, **kwargs):
        print("inside processing")
        index = ConvertView.construct_index("media")
        return render(request, 'dashboard/convert.html')

    def chatbot(input_text):
        index = GPTSimpleVectorIndex.load_from_disk('index.json')
        response = index.query(input_text, response_mode="compact")
        return response.response

