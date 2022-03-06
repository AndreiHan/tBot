FROM python:slim

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy Project Files
COPY tools /tools/
COPY storage /storage/
COPY main.py  ./
# Run the application:
ENTRYPOINT ["tail", "-f", "/dev/null"]