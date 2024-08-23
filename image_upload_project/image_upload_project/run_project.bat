@echo off
start cmd /k "cd image_upload_project && python manage.py runserver"
start cmd /k "cd image-upload-frontend && npm start"
