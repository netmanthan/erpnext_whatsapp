## Whatsapp Integration for ERPNext

### Whatsapp Settings doctype
![Captura de Pantalla 2019-11-05 a la(s) 14 55 26](https://user-images.githubusercontent.com/46027152/68233033-22e81080-ffdd-11e9-915f-6ecf946b634c.png)

### New button "Send Whatsapp" in SMS Center
![Captura de Pantalla 2019-11-05 a la(s) 14 56 16](https://user-images.githubusercontent.com/46027152/68233034-22e81080-ffdd-11e9-9ce6-64c048586e09.png)

### New option "Whatsapp" (and Attach Document Print) in "Send SMS" dialog
![66226881-405e4d80-e6b2-11e9-8692-c72e69eedf8c](https://user-images.githubusercontent.com/46027152/68233035-22e81080-ffdd-11e9-9a64-93cc4d5635ab.png)

## Installation Guide
First you have to get the app:
```shell
bench get-app git@github.com:fproldan/erpnext_whatsapp.git
```
Then, you should double check for the requirements to be ready:
```shell
bench update --requirements
bench build
```
And for the last step, you should install the app in you site:
```shell
bench --site SITE_NAME install-app whatsapp_integration
```

## Whatsapp for Business limitations
- WhatsApp requires that your application implement [explicit user opt-ins](https://developers.facebook.com/docs/whatsapp/guides/opt-in/) to deliver messages over WhatsApp .
- You always should start the comunication with a template message aproved by Whatsapp. To read more about templates, click [here](https://developers.facebook.com/docs/whatsapp/message-templates/creation/).
- After the client sends you a message, you have 24hs to send whatever you want (not only template messages).
