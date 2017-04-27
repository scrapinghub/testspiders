FROM scrapinghub/scrapinghub-stack-scrapy:1.3
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app
RUN python setup.py install
