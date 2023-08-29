FROM python:3.9-slim

HEALTHCHECK NONE

WORKDIR /app
COPY . .

ENV AUTHOR=DanilAkm
ENV UUID=eccc0842-ee3a-43ef-9ecb-c5c004011008

EXPOSE 8000


RUN chmod g-s /usr/bin/wall /usr/sbin/unix_chkpwd \
    /usr/bin/expiry /usr/bin/chage   
RUN chmod u-s /usr/bin/su /usr/bin/newgrp /usr/bin/passwd /usr/bin/chsh \ 
    /usr/bin/gpasswd /usr/bin/mount /usr/bin/umount /usr/bin/chfn


RUN useradd -d /home/dockle -m -s /bin/bash lalka
USER lalka

CMD ["python", "cloud_webapp.py"]
