FROM scrapinghub/scrapinghub-stack-scrapy:1.4
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ENV SCRAPY_SETTINGS_MODULE testspiders.settings
COPY . /app
RUN python setup.py install
RUN echo "echo py:testargs.py" > /usr/sbin/shub-list-scripts && \
    chmod +x /usr/sbin/shub-list-scripts
