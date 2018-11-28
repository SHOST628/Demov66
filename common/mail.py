from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from common.logger import logger


class Mail:
    def __init__(self, host, user, passwd):
        self._user = user
        try:
            server = smtplib.SMTP()
            server.connect(host,25)
            server.login(user, passwd)
            self._server = server
        except Exception as e:
            logger.error("登陆邮件服务器失败")
            logger.exception(e)

    def send_mail(self, to_addrs, sub, content, attach_path='', attach_type='', subtype ='plain'):
        """
        it can send a text or html email with an attachment or many of attachments
        :param to_addrs: the address from receiver
        :param sub: subject name
        :param content: email message
        :param attach_path: attachment path
        eg: D:\javawork\PyTest\src\main.py  or  D:\javawork\PyTest\src\main.py,D:\javawork\PyTest\src\test.jpg
        :param attach_type: image,noimage  decide  if the file is an image or an other attachment
        :param subtype: html file : html   ;   text file: plain
        :return:
        """
        if attach_path == '':
            msg = MIMEText(content, _subtype=subtype, _charset='utf-8')
        else:
            msg = MIMEMultipart()
            f_path_list = attach_path.split(',')
            for f_path in f_path_list:
                try:
                    if '\\' in f_path:
                        index = f_path.rindex('\\')
                    else:
                        index = f_path.rindex('/')
                    file_name = f_path[index + 1:]
                    if attach_type == 'image':
                        att = MIMEImage(open(attach_path, 'rb').read())
                        att['Content-Disposition'] = 'attachment; filename="%s"' % file_name
                        msg.attach(att)

                    else:
                        att = MIMEText(open(attach_path, 'rb').read(), 'base64', 'utf-8')
                        att['Content-Type'] = 'application/octet-stream'
                        att['Content-Disposition'] = 'attachment; filename="%s"' % file_name
                        msg.attach(att)
                        # add email message
                        msg.attach(MIMEText(content, _subtype=subtype, _charset='utf-8'))
                except Exception as e:
                    logger.exception(e)

        msg['Subject'] = sub
        msg['From'] = self._user
        msg['To'] = to_addrs
        to_addr_list = to_addrs.split(',')

        try:
            self._server.sendmail(self._user, to_addr_list, msg.as_string())
            logger.info("发送了一封主题为 《%s》 的邮件给 %s , 邮件明细: %s " % (sub, to_addr_list,content))
        except Exception as e:
            logger.error('邮件发送失败')
            logger.exception(e)

    def __del__(self):
        self._server.quit()
        self._server.close()
