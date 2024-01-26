from envelopes import Envelope, GMailSMTP
try:
    envelope = Envelope(
        from_addr=(u'farhanmushtaque13@gamil.com', u'From Example'),
        to_addr=(u'mdfarhanofficial@protonmail.com', u'To Example'),
        subject=u'Envelopes demo',
        text_body=u"I'm a helicopter!"
    )
    print("Wait! we sending your mail .....")
# envelope.add_attachment('/Users/bilbo/Pictures/helicopter.jpg')

# Send the envelope using an ad-hoc connection...
    envelope.send('smtp-relay.gmail.com', login='farhanmushtaque13@gamil.com',password="idon'tlikeCoding$", tls=True)

# Or send the envelope using a shared GMail connection...
    # gmail = GMailSMTP('farhanmushtaque13@gamil.com', "idon'tlikeCoding$")
    # gmail.send(envelope)
    print('Email sent succesfully')
except:
    print('Failed to send email :(')
