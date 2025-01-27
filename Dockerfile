# استخدام Python الرسمي
FROM python:3.10-slim

# تحديد مسار العمل
WORKDIR /app

# نسخ الملفات
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# تشغيل التطبيق
CMD ["python", "app.py"]
