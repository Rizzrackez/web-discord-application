import time
import webhook


def send_to_webhook_movie_trigger():
    while True:
        webhook.send_user_id("movie")
        time.sleep(60)


if __name__ == '__main__':
    send_to_webhook_movie_trigger()