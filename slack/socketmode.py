import os
import logging
import sys

from dotenv import dotenv_values

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

config = dotenv_values(".env")  # take environment variables from .env.

logging.basicConfig(level=logging.INFO)  # set logging level

app = App(token=config["XOXB"])  # get app object slash commands to work


@app.command('/'+config["MACHINE"]+'-hello')
def hello(ack, body, logger):
    logger.debug(body)
    user_id = body['user_id']
    ack(f'Hi, <@{user_id}>!')
    logger.info('Success')


@app.command('/'+config["MACHINE"]+'-get-status')
def get_status(ack, body, logger):
    logger.debug(body)
    ack(f'Status: Running\nExperiment name : TEST EXPERIMENT')
    logger.info('Success')


@app.command('/'+config["MACHINE"]+'-get-pics')
def get_pics(ack, body, logger):
    logger.debug(body)

    # Slack setup
    client = WebClient(token=config["XOXB"])

    # get list of pics file names/paths
    path = os.path.abspath(config["EXP_PATH"])
    try:
        pics = [pic for pic in os.listdir(path) if (os.path.isfile(
            os.path.join(path, pic)) and pic.endswith('.png'))]
    except FileNotFoundError as e:
        ack(f'Oops. We couldn\'t find the pictures we were looking for. Please check server logs.')
        logger.error(e)
    except:
        ack(f'Oops. We couldn\'t find the pictures we were looking for. Please check server logs.')
        logger.error(sys.exc_info()[0])
    else:
        pic_paths = [os.path.join(config["EXP_PATH"], pic)
                     for pic in pics]

        # for each pic in all position dirs this experiment has
        try:
            if(len(pic_paths) == 0):
                ack(f'Couldn\'t find any recent pictures to send. Please check server logs.')
                logger.error('Length of pic_paths is 0')
            else:
                ack(f'Here are some recent pictures!')
                for pic in pic_paths:
                    # Upload file
                    file_name = pic
                    try:
                        result = client.files_upload(
                            channels=config["CHANNEL_ID"],
                            file=file_name
                        )
                    except SlackApiError as e:
                        ack(f'An exception occured on the server-side. Please check server logs.')
                        logger.error(e)
                logger.info('Success')
        except:
            ack(f'An exception occured on the server-side. Please check server logs.')
            logger.error(sys.exc_info()[0])


if __name__ == '__main__':
    SocketModeHandler(app, config["XAPP"]).start()
