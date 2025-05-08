from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import os
import pdfplumber
import logging

# Create a logger instance
logger = logging.getLogger('pdfextractor')

def extract_pdfs(request):
    try:
        pdf_dir = os.path.join(settings.BASE_DIR, 'pdfs')  # directory holding PDF files
        result = []
        
        if not os.path.exists(pdf_dir):
            return JsonResponse({"error": "PDF folder not found."}, status=404)

        for filename in os.listdir(pdf_dir):
            if filename.lower().endswith('.pdf'):
                pdf_path = os.path.join(pdf_dir, filename)
                with pdfplumber.open(pdf_path) as pdf:
                    all_text = ''
                    for page in pdf.pages:
                        all_text += page.extract_text() or ''

                result.append({
                    "filename": filename,
                    "content": all_text.strip()
                })

        return JsonResponse(result, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 2})
    except Exception as e:
        logger.error(f"Error occurred in extract_view: {str(e)}", exc_info=True)
        return JsonResponse({"error": "Internal server error"}, status=500)
