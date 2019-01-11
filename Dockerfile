FROM scrapinghub/scrapinghub-stack-scrapy:1.4
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ENV SCRAPY_SETTINGS_MODULE testspiders.settings
COPY shub-list-scripts /usr/sbin/
RUN chmod +x /usr/sbin/shub-list-scripts
COPY . /app
RUN python setup.py install
