## discord_message_sender

### Установка

```bash
pip install -r requirements.txt
```

### Запуск

```bash
python main.py
```

### Конфиг

Конфиг находится в файле `Config.yaml`

```yaml
discord:
  profiles:
    - name: имя | maxrbv
      token: токен | asdasdasd234234
      channel_id: id канала | 37491294124
      messages: имя txt файла | messages.txt
      timeout: пауза между сообщениями в секундах | 300
      proxy: прокси | 'http://юзер:пароль@ip:порт'
    - name: имя | maxrbv
      token: токен | asdasdasd234234
      channel_id: id канала | 37491294124
      messages: имя txt файла | messages.txt
      timeout: пауза между сообщениями в секундах | 300
      proxy: прокси | 'http://юзер:пароль@ip:порт'
```

### Сообщения

Сообщения находятся в файле `assets/messages.txt`

```txt
Тут
в строчку
сообщения
```

### Суть работы

Скрипт отправляет сообщения в дискорд с указаным id канала раз в указанное время с рандомным сообщением из файла.

