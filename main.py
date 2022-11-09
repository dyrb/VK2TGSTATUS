from pyrogram import Client
import time
import vk_api

# VK API TOKEN  https://vkhost.github.io/  https://vk.com/editapp?act=create
vk = vk_api.VkApi(token="")

# Telegram Info Main https://my.telegram.org/apps
api_id = 000 # Ваш APP ID
api_hash = "daskdsak3849"
app = Client("my_account", api_id=api_id, api_hash=api_hash)
# Telegram Info END


async def main():
        await app.start()
        while True:
            #VK API Get Status
            vk_status = vk.method("status.get")
            vk_status_text = vk_status['text']
            # Telegram API Update Status
            await app.update_profile(bio="Сейчас слушаю: " + vk_status_text)
            time.sleep(20)

app.run(main())