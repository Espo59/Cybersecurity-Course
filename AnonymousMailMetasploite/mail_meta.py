import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_interactive_email():
    # --- Configuration ---
    # target_ip: The IP address of the target machine (e.g., Metasploitable)
    # target_port: Standard SMTP port (25) which is often left open on vulnerable systems
    target_ip = "192.168..."  
    target_port = 25

    print("--- SMTP Automation Tool for Metasploitable ---")
    
    # --- Interactive User Inputs ---
    # In a real scenario, 'sender' can be spoofed as SMTP doesn't always verify the identity
    sender = input("From (e.g., admin@secret.com): ")
    receiver = input("To (e.g., sys): ")
    subject = input("Subject: ")
    print("Enter your message (Press Ctrl+D or Ctrl+Z on Windows then Enter when finished):")
    
    # Logic to handle multi-line inputs until EOF (End Of File) character
    body_lines = []
    while True:
        try:
            line = input()
            body_lines.append(line)
        except EOFError:
            break
    body = "\n".join(body_lines)

    # --- Constructing the Email Structure using MIME ---
    # MIMEMultipart allows us to bundle the subject, headers, and body into a valid format
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    
    # Attach the body text as 'plain' (non-HTML) text
    msg.attach(MIMEText(body, 'plain'))

    try:
        print(f"\n[+] Connecting to {target_ip} on port {target_port}...")
        
        # Establishing a raw TCP connection for SMTP
        # By default, this tool does not use TLS/SSL as Metasploitable services are usually plain text
        server = smtplib.SMTP(target_ip, target_port)
        
        # Send the mail: it requires the sender, a list of recipients, and the formatted string
        server.sendmail(sender, [receiver], msg.as_string())
        
        print(f"[+] Success! Email successfully queued/sent to {receiver}.")
        
        # Cleanly close the SMTP session
        server.quit()
        
    except ConnectionRefusedError:
        print("[-] Error: Connection refused. Is the SMTP service running on the target?")
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")

if __name__ == "__main__":
    send_interactive_email()
