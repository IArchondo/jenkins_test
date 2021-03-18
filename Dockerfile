FROM python:3.7
COPY . /python-test
WORKDIR /python-test
RUN pip install - requirements.txt
RUN ["pytest","-v","--junitxml=reports/result.xml"]
CMD tail -f /dev/null