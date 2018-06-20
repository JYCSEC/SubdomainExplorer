#JYCsec
import dns
from dns import resolver

#TODO Implement as cronjob or persistent python job
r=resolver.Resolver
sites= open("sites.txt","r")
for line in sites:
    words open("wordlist.txt","r")
        for sd in words:
            fqdn=sd.rstrip('\n') + line.rstrip('\n')
            try:
                a= r.query(fqdn,"A")
                cname= r.query(fqdn,"CNAME")
                print fqdn
                for i in a:
                    print i
                for i in cname:
                    print i
            except Exception:
                pass
#            ns= r.query(fqdn,"NS")
#            for i in ns:
#                print i
#TODO sort based on page not found & discovery of Github, Heroku, Unbounce, Tumblr, Shopify, Instapage, Desk, Tictail, Campaignmonitor, Cargocollective, Statuspage, Amazonaws, Cloudfront, Bitbucket, Smartling, Acquia, Fastly, Pantheon, Zendesk, Uservoice, Ghost, Freshdesk, Pingdom, Tilda, WordPress, Teamwork, Helpjuice, Helpscout, Cargo, Feedpress, Surge, Surveygizmo, Mashery, Intercom, Webflow, Kajabi, Thinkific, Tave, Wishpond, Aftership, Aha, Brightcove, Bigcartel, Activecompaign, Compaignmonitor, Acquia, Proposify, Simplebooklet, Getresponse, Vend, Jetbrains, Azure

#TODO output to log file with importance rating
