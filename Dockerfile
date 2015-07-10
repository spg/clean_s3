FROM python:2.7.7

RUN pip install boto

ENTRYPOINT ["python"]

CMD ["/clean_s3.py"]

COPY clean_s3.py /
