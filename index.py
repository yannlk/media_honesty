import praw
import csv
import tldextract
import message
import automation

# initialize reddit connection
reddit = praw.Reddit(client_id="", client_secret="",
                     username="media_honesty", password="", user_agent="Anti Propaganda, u/yolkyboii")

f = open("bias_reliability.csv")

print("100% Loaded :)")

while True:

    for mention in reddit.inbox.mentions(limit=3):  # cycle through inbox

        if mention.new:

            print(mention.created_utc, mention.author, mention.submission.domain)

            long = tldextract.extract(mention.submission.domain)
            domain = long.domain + "." + long.suffix  # standardise domain

            f.seek(0, 0)  # reset file reading
            found_in_db = False

            for row in csv.reader(f):  # check through db to find source

                long = tldextract.extract(row[0])
                input_dom = long.domain + "." + long.suffix

                if input_dom == domain:  # if found source in db

                    if mention.author is not None:
                        mention.reply(message.msg(row))

                    mention.mark_read()
                    found_in_db = True

                    automation.append_db("statistics.csv", domain)

                    print("success", row[1])
                    break

            if not found_in_db:

                if mention.author is not None:
                    mention.reply(message.n_db(domain))

                automation.append_db("not_in_db.csv", domain)

                print(domain, "was not in database")

            mention.mark_read()

            in_db = False
