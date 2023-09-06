class Email_Handler():
    def send_email(self, subject: str, body: str, recipient: str):
        try:
            import win32com.client as win32
            outlook = win32.Dispatch("Outlook.Application")
            mail = outlook.CreateItem(0)  # 0 represents the message type for a new email

            # Set email properties
            mail.Subject = subject
            mail.Body = body
            mail.To = recipient

            # Send the email
            mail.Send()

            print("Email sent successfully!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")