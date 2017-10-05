# import requests
# import json
# from urllib import request, parse
# import os
# from random import randrange
#
from bot_box.features import request, parse, os, randrange, json

GOOGLE_IMAGE_API_KEY = os.environ.get("GOOGLE_IMAGE_API_KEY")
IMAGE_SEARCH_ENGINE_ID = os.environ.get("IMAGE_SEARCH_ENGINE_ID")

''' google custom search sample result

    {
        "kind": "customsearch#search",
        "url": {
            "type": "application/json",
            "template": "https://www.googleapis.com/customsearch/v1?q={searchTerms}&num={count?}&start={startIndex?}&lr={language?}&safe={safe?}&cx={cx?}&sort={sort?}&filter={filter?}&gl={gl?}&cr={cr?}&googlehost={googleHost?}&c2coff={disableCnTwTranslation?}&hq={hq?}&hl={hl?}&siteSearch={siteSearch?}&siteSearchFilter={siteSearchFilter?}&exactTerms={exactTerms?}&excludeTerms={excludeTerms?}&linkSite={linkSite?}&orTerms={orTerms?}&relatedSite={relatedSite?}&dateRestrict={dateRestrict?}&lowRange={lowRange?}&highRange={highRange?}&searchType={searchType}&fileType={fileType?}&rights={rights?}&imgSize={imgSize?}&imgType={imgType?}&imgColorType={imgColorType?}&imgDominantColor={imgDominantColor?}&alt=json"
        },
        "queries": {
            "request": [
                {
                    "title": "Google Custom Search - modi",
                    "totalResults": "12700000",
                    "searchTerms": "modi",
                    "count": 10,
                    "startIndex": 1,
                    "inputEncoding": "utf8",
                    "outputEncoding": "utf8",
                    "safe": "off",
                    "cx": "000300568862861334301:-a3dhnrxpq0"
                }
            ],
            "nextPage": [
                {
                    "title": "Google Custom Search - modi",
                    "totalResults": "12700000",
                    "searchTerms": "modi",
                    "count": 10,
                    "startIndex": 11,
                    "inputEncoding": "utf8",
                    "outputEncoding": "utf8",
                    "safe": "off",
                    "cx": "000300568862861334301:-a3dhnrxpq0"
                }
            ]
        },
        "context": {
            "title": "bot_image_search"
        },
        "searchInformation": {
            "searchTime": 0.783913,
            "formattedSearchTime": "0.78",
            "totalResults": "12700000",
            "formattedTotalResults": "12,700,000"
        },
        "items": [
            {
                "kind": "customsearch#result",
                "title": "Narendra Modi - Wikipedia",
                "htmlTitle": "Narendra <b>Modi</b> - Wikipedia",
                "link": "https://en.wikipedia.org/wiki/Narendra_Modi",
                "displayLink": "en.wikipedia.org",
                "snippet": "Narendra Damodardas Modi is an Indian politician who is the 14th and current \nPrime Minister of India, in office since May 2014. He was the Chief Minister of ...",
                "htmlSnippet": "Narendra Damodardas <b>Modi</b> is an Indian politician who is the 14th and current <br>\nPrime Minister of India, in office since May 2014. He was the Chief Minister of&nbsp;...",
                "cacheId": "shVMqZscVTUJ",
                "formattedUrl": "https://en.wikipedia.org/wiki/Narendra_Modi",
                "htmlFormattedUrl": "https://en.wikipedia.org/wiki/Narendra_<b>Modi</b>",
                "pagemap": {
                    "hcard": [
                        {
                            "fn": "Narendra Modi",
                            "nickname": "Narendra Damodardas Modi",
                            "bday": "1950-09-17",
                            "label": "7, Lok Kalyan Marg, New Delhi"
                        },
                        {
                            "fn": "Narendra Modi"
                        }
                    ],
                    "cse_thumbnail": [
                        {
                            "width": "204",
                            "height": "247",
                            "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIBXlew2RwQ42hN7TEMhruWi0yd9fVWNPDGUf38oNUB5IN8q7GZEhDo6-M"
                        }
                    ],
                    "metatags": [
                        {
                            "referrer": "origin-when-cross-origin",
                            "og:image": "https://upload.wikimedia.org/wikipedia/commons/9/90/PM_Modi_2015.jpg"
                        }
                    ],
                    "cse_image": [
                        {
                            "src": "https://upload.wikimedia.org/wikipedia/commons/9/90/PM_Modi_2015.jpg"
                        }
                    ]
                }
            },
            {
                "kind": "customsearch#result",
                "title": "Narendra Modi (@narendramodi) | Twitter",
                "htmlTitle": "Narendra <b>Modi</b> (@narendramodi) | Twitter",
                "link": "https://twitter.com/narendramodi",
                "displayLink": "twitter.com",
                "snippet": "15.5K tweets • 2649 photos/videos • 30.8M followers. \"Met Shri Ram Nath Kovind. \nhttps://t.co/fM9fg5mAnA\"",
                "htmlSnippet": "15.5K tweets • 2649 photos/videos • 30.8M followers. &quot;Met Shri Ram Nath Kovind. <br>\nhttps://t.co/fM9fg5mAnA&quot;",
                "cacheId": "mmxjyszD0b4J",
                "formattedUrl": "https://twitter.com/narendramodi",
                "htmlFormattedUrl": "https://twitter.com/narendra<b>modi</b>",
                "pagemap": {
                    "cse_thumbnail": [
                        {
                            "width": "261",
                            "height": "193",
                            "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQvFjnEm19GtCiC9s_PHBKDWBGdbDcFyvUp_v0S78d7FrJls8Oyhno-G6NJ"
                        }
                    ],
                    "metatags": [
                        {
                            "msapplication-tileimage": "//abs.twimg.com/favicons/win8-tile-144.png",
                            "msapplication-tilecolor": "#00aced",
                            "swift-page-name": "profile",
                            "swift-page-section": "profile",
                            "al:ios:url": "twitter://user?screen_name=narendramodi",
                            "al:ios:app_store_id": "333903271",
                            "al:ios:app_name": "Twitter",
                            "al:android:url": "twitter://user?screen_name=narendramodi",
                            "al:android:package": "com.twitter.android",
                            "al:android:app_name": "Twitter"
                        }
                    ],
                    "cse_image": [
                        {
                            "src": "https://pbs.twimg.com/media/DCsZxbRUIAAzANp.jpg"
                        }
                    ]
                }
            },
            {
                "kind": "customsearch#result",
                "title": "Three years of Narendra Modi government | India | Al Jazeera",
                "htmlTitle": "Three years of Narendra <b>Modi</b> government | India | Al Jazeera",
                "link": "http://www.aljazeera.com/indepth/features/2017/05/years-narendra-modi-government-170525083111566.html",
                "displayLink": "www.aljazeera.com",
                "snippet": "May 28, 2017 ... Modi promised employment to millions of youth who join the job market every \nyear, and to end corruption. In the past three years, more jobs ...",
                "htmlSnippet": "May 28, 2017 <b>...</b> <b>Modi</b> promised employment to millions of youth who join the job market every <br>\nyear, and to end corruption. In the past three years, more jobs&nbsp;...",
                "cacheId": "bYNEECi-FkMJ",
                "formattedUrl": "www.aljazeera.com/.../years-narendra-modi-government-170525083111566. html",
                "htmlFormattedUrl": "www.aljazeera.com/.../years-narendra-<b>modi</b>-government-170525083111566. html",
                "pagemap": {
                    "cse_thumbnail": [
                        {
                            "width": "300",
                            "height": "168",
                            "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRaJYw3PqaApvE5FM7fa2NLgqhXxSAQYHS_fW6-9gph-PeMNBgqODvRBdo"
                        }
                    ],
                    "metatags": [
                        {
                            "viewport": "width=device-width, initial-scale=1.0, minimum-scale=1.0 maximum-scale=1.0, minimal-ui",
                            "guid": "170525083111566",
                            "title": "Three years of Narendra Modi government",
                            "author": "Shriya Ramakrishnan",
                            "og:title": "Three years of Narendra Modi government",
                            "og:description": "As the BJP government completes three years in office, Al Jazeera looks at the progress made so far.",
                            "og:url": "http://www.aljazeera.com/indepth/features/2017/05/years-narendra-modi-government-170525083111566.html",
                            "url": "http://www.aljazeera.com/indepth/features/2017/05/years-narendra-modi-government-170525083111566.html",
                            "og:internalurl": "http://www.aljazeera.com/indepth/features/2017/05/years-narendra-modi-government-170525083111566.html",
                            "shorturl": "http://aje.io/qqbw",
                            "og:image": "http://www.aljazeera.com/mritems/Images/2017/5/25/c07978557e7c459e8bf32e8743a210ec_18.jpg",
                            "image": "http://www.aljazeera.com/mritems/Images/2017/5/25/c07978557e7c459e8bf32e8743a210ec_18.jpg",
                            "twitter:title": "Three years of Narendra Modi government",
                            "lastmodifieddate": "Sun, 28 May 2017 14:52:21 GMT",
                            "twitter:image": "http://www.aljazeera.com/mritems/Images/2017/5/25/c07978557e7c459e8bf32e8743a210ec_18.jpg",
                            "twitter:description": "As the BJP government completes three years in office, Al Jazeera looks at the progress made so far.",
                            "contenttype": "Feature",
                            "contentindexurl": "/indepth/features/",
                            "twitter:account_id": "4970411",
                            "twitter:card": "summary_large_image",
                            "google-play-app": "app-id=net.aljazeera.english",
                            "twitter:site": "@AJEnglish"
                        }
                    ],
                    "cse_image": [
                        {
                            "src": "http://www.aljazeera.com/mritems/Images/2017/5/25/c07978557e7c459e8bf32e8743a210ec_18.jpg"
                        }
                    ]
                }
            },
            {
                "kind": "customsearch#result",
                "title": "Narendra Modi - Home | Facebook",
                "htmlTitle": "Narendra <b>Modi</b> - Home | Facebook",
                "link": "https://www.facebook.com/narendramodi/",
                "displayLink": "www.facebook.com",
                "snippet": "Narendra Modi. 42217774 likes · 969810 talking about this. Prime Minister of \nIndia.",
                "htmlSnippet": "Narendra <b>Modi</b>. 42217774 likes · 969810 talking about this. Prime Minister of <br>\nIndia.",
                "cacheId": "40bYoFRhVsMJ",
                "formattedUrl": "https://www.facebook.com/narendramodi/",
                "htmlFormattedUrl": "https://www.facebook.com/narendra<b>modi</b>/",
                "pagemap": {
                    "metatags": [
                        {
                            "referrer": "default",
                            "al:android:app_name": "Facebook",
                            "al:android:package": "com.facebook.katana",
                            "al:android:url": "fb://page/177526890164?referrer=app_link",
                            "al:ios:app_name": "Facebook",
                            "al:ios:app_store_id": "284882215",
                            "al:ios:url": "fb://page/?id=177526890164",
                            "og:title": "Narendra Modi",
                            "og:description": "Narendra Modi. 42,217,774 likes · 969,810 talking about this. Prime Minister of India.",
                            "og:image": "https://scontent-atl3-1.xx.fbcdn.net/v/t1.0-1/12920234_10156879922780165_1562561844037541137_n.jpg?oh=caf420afa7e06402f2e65c51a791dbbc&oe=59DAC797",
                            "og:url": "https://www.facebook.com/narendramodi/"
                        }
                    ],
                    "cse_image": [
                        {
                            "src": "https://scontent-atl3-1.xx.fbcdn.net/v/t1.0-1/12920234_10156879922780165_1562561844037541137_n.jpg?oh=caf420afa7e06402f2e65c51a791dbbc&oe=59DAC797"
                        }
                    ]
                }
            },
            {
                "kind": "customsearch#result",
                "title": "Narendra Modi",
                "htmlTitle": "Narendra <b>Modi</b>",
                "link": "http://www.narendramodi.in/",
                "displayLink": "www.narendramodi.in",
                "snippet": "Official website of Narendra Modi. ... Toggle navigation. Narendra Modi · \nDownload App App Download. Login / Register. X ...",
                "htmlSnippet": "Official website of Narendra <b>Modi</b>. ... Toggle navigation. Narendra <b>Modi</b> &middot; <br>\nDownload App App Download. Login / Register. X&nbsp;...",
                "cacheId": "-CrTl5Vmz94J",
                "formattedUrl": "www.narendramodi.in/",
                "htmlFormattedUrl": "www.narendra<b>modi</b>.in/",
                "pagemap": {
                    "cse_thumbnail": [
                        {
                            "width": "246",
                            "height": "205",
                            "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrn5FvMnK622sGC68TIMdlLt1a_mzYT6O1y6XUl1oJzTSwbfYTBa1eNKA6"
                        }
                    ],
                    "metatags": [
                        {
                            "fb:pages": "177526890164",
                            "og:title": "Home  |  www.narendramodi.in |",
                            "og:type": "Home",
                            "og:url": "http://www.narendramodi.in/",
                            "og:site_name": "www.narendramodi.in",
                            "twitter:card": "summary_large_image",
                            "twitter:site": "@narendramodi",
                            "twitter:creator": "@narendramodi",
                            "twitter:title": "Home  |  www.narendramodi.in |",
                            "twitter:description": "Official website of Narendra Modi",
                            "twitter:url": "http://www.narendramodi.in/",
                            "viewport": "width=device-width, initial-scale=1.0, maximum-scale=1.0"
                        }
                    ],
                    "cse_image": [
                        {
                            "src": "http://cdn.narendramodi.in/cmsuploads/0.85113100_1497424237_566x473-2-1.jpg"
                        }
                    ]
                }
            },
            {
                "kind": "customsearch#result",
                "title": "Narendra Modi: Latest News of PM Narendra Modi, Photos & Videos",
                "htmlTitle": "Narendra <b>Modi</b>: Latest News of PM Narendra <b>Modi</b>, Photos &amp; Videos",
                "link": "http://timesofindia.indiatimes.com/topic/Narendra-Modi",
                "displayLink": "timesofindia.indiatimes.com",
                "snippet": "Narendra Damodardas Modi is the fourteenth Prime Minister of India, who took \noffice on May 26, 2014. Before assuming office as the Prime Minister of India, ...",
                "htmlSnippet": "Narendra Damodardas <b>Modi</b> is the fourteenth Prime Minister of India, who took <br>\noffice on May 26, 2014. Before assuming office as the Prime Minister of India,&nbsp;...",
                "cacheId": "D-VOJ53mFDUJ",
                "formattedUrl": "timesofindia.indiatimes.com/topic/Narendra-Modi",
                "htmlFormattedUrl": "timesofindia.indiatimes.com/topic/Narendra-<b>Modi</b>",
                "pagemap": {
                    "cse_thumbnail": [
                        {
                            "width": "200",
                            "height": "200",
                            "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQlu1-YxTppfllqNRPlk8OxDwMr-O4nQOYoJ25g657VFKlurtuGQ9_aGG0"
                        }
                    ],
                    "imageobject": [
                        {
                            "url": "http://timesofindia.indiatimes.com/photo/msid-58127550/toilogo.jpg",
                            "width": "600",
                            "height": "60"
                        }
                    ],
                    "organization": [
                        {
                            "name": "The Times of India",
                            "url": "http://timesofindia.indiatimes.com"
                        }
                    ],
                    "metatags": [
                        {
                            "og:site_name": "The Times of India",
                            "og:type": "website",
                            "fb:admins": "556964827,1449503695",
                            "fb:app_id": "117787264903013",
                            "y_key": "b1abb36a8d5c19c9",
                            "og:title": "Narendra Modi: Latest News, Videos and  Photos | Times of India",
                            "twitter:title": "Narendra Modi: Latest News, Videos and  Photos | Times of India",
                            "og:description": "Latest Narendra Modi News, Photos, Blogposts, Videos and Wallpapers. Explore Narendra Modi profile at Times of India",
                            "twitter:description": "Latest Narendra Modi News, Photos, Blogposts, Videos and Wallpapers. Explore Narendra Modi profile at Times of India",
                            "og:url": "http://timesofindia.indiatimes.com/topic/Narendra-Modi",
                            "twitter:url": "http://timesofindia.indiatimes.com/topic/Narendra-Modi",
                            "og:image": "http://timesofindia.indiatimes.com/photo/10230125.cms",
                            "twitter:image": "http://timesofindia.indiatimes.com/photo/10230125.cms",
                            "viewport": "width=device-width, height=device-height,initial-scale=1.0,user-scalable=no",
                            "last-modified": "Monday, 19 June, 2017 08:16:56PM",
                            "last-modified-date": "Mon, Jun 19, 2017",
                            "last-modified-time": "08.16PM IST",
                            "position": "1"
                        }
                    ],
                    "cse_image": [
                        {
                            "src": "http://timesofindia.indiatimes.com/photo/10230125.cms"
                        }
                    ]
                }
            },
            {
                "kind": "customsearch#result",
                "title": "John Elliott: Does India's Modi Deserve to be Reelected?",
                "htmlTitle": "John Elliott: Does India&#39;s <b>Modi</b> Deserve to be Reelected?",
                "link": "http://www.newsweek.com/john-elliott-does-indias-modi-deserve-be-reelected-617056",
                "displayLink": "www.newsweek.com",
                "snippet": "May 29, 2017 ... The third anniversary of Narendra Modi being sworn in as prime minister was \ncelebrated on May 26 with all the bombast that has come to ...",
                "htmlSnippet": "May 29, 2017 <b>...</b> The third anniversary of Narendra <b>Modi</b> being sworn in as prime minister was <br>\ncelebrated on May 26 with all the bombast that has come to&nbsp;...",
                "cacheId": "lnc9WEzIy5oJ",
                "formattedUrl": "www.newsweek.com/john-elliott-does-indias-modi-deserve-be-reelected- 617056",
                "htmlFormattedUrl": "www.newsweek.com/john-elliott-does-indias-<b>modi</b>-deserve-be-reelected- 617056",
                "pagemap": {
                    "cse_thumbnail": [
                        {
                            "width": "275",
                            "height": "183",
                            "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqvv93u81Elp2uWJyF3KUItJS_PBLSVUSxLYv82HEwuNo2f8xITiIbABEu"
                        }
                    ],
                    "imageobject": [
                        {
                            "url": "http://s.newsweek.com/sites/www.newsweek.com/themes/newsweek/images/logo.png?v=1"
                        }
                    ],
                    "person": [
                        {
                            "url": "John Elliott",
                            "name": "John Elliott"
                        }
                    ],
                    "organization": [
                        {
                            "name": "Newsweek"
                        }
                    ],
                    "metatags": [
                        {
                            "viewport": "width=device-width, initial-scale=1.0, maximum-scale=1, user-scalable=no",
                            "news_keywords": "cows, beef, ban, buffalo, bjp, muslim, hindu, bangladesh, china, sri lanka, border, pakistan, afghanistan,",
                            "fb:app_id": "245537789135954",
                            "og:type": "article",
                            "og:site_name": "Newsweek",
                            "og:url": "http://www.newsweek.com/john-elliott-does-indias-modi-deserve-be-reelected-617056",
                            "og:title": "John Elliott: Does India’s Modi deserve to be reelected?",
                            "og:description": "The new law on the slaughter of cows and buffalos is not so much an animal welfare as a religious issue.",
                            "og:image": "http://s.newsweek.com/sites/www.newsweek.com/files/2017/05/29/gettyimages-487385691.jpg",
                            "article:publisher": "https://www.facebook.com/Newsweek",
                            "article:section": "Opinion",
                            "article:modified_time": "2017-06-03T11:16:02-04:00",
                            "article:published_time": "2017-05-29T10:18:51-04:00",
                            "twitter:site": "@newsweek",
                            "twitter:card": "summary_large_image",
                            "twitter:title": "John Elliott: Does India’s Modi deserve to be reelected?",
                            "twitter:url": "http://www.newsweek.com/john-elliott-does-indias-modi-deserve-be-reelected-617056",
                            "twitter:description": "The new law on the slaughter of cows and buffalos is not so much an animal welfare as a religious issue.",
                            "twitter:image": "http://s.newsweek.com/sites/www.newsweek.com/files/styles/full/public/2017/05/29/gettyimages-487385691.jpg",
                            "msapplication-tilecolor": "#ff0000",
                            "msapplication-tileimage": "http://s.newsweek.com/sites/www.newsweek.com/themes/newsweek/favicons/mstile-144x144.png",
                            "msapplication-config": "http://s.newsweek.com/sites/www.newsweek.com/themes/newsweek/favicons/browserconfig.xml",
                            "com.silverpop.brandeddomains": "www.pages06.net,aidataconf.com,amp.ibtimes.co.uk,e-amp.newsweek.com,e-sns.newsweek.com,europe.newsweek.com,events.newsweek.com,ibt-dev.co.uk,ibtimes.co.uk,ibtimes.com,idigitaltimes.com,latintimes.com,medicaldaily.com,newsweek.com,player.one,sns.europe.newsweek.com,sns.ibtimes.co.uk,subscription.newsweek.com,www.ibt-dev.co.uk,www.ibtimes.co.uk,www.ibtimes.com",
                            "fb:pages": "18343191100"
                        }
                    ],
                    "webpage": [
                        {
                            "relatedlink": "John Elliott: May and Modi Benefit From Weak Opponents"
                        }
                    ],
                    "cse_image": [
                        {
                            "src": "http://s.newsweek.com/sites/www.newsweek.com/files/2017/05/29/gettyimages-487385691.jpg"
                        }
                    ],
                    "newsarticle": [
                        {
                            "mainentityofpage": "http://www.newsweek.com/john-elliott-does-indias-modi-deserve-be-reelected-617056",
                            "headline": "John Elliott: Does India’s Modi Deserve to be Reelected?",
                            "datepublished": "2017-05-29T10:18:51-04:00",
                            "datemodified": "2017-06-03T11:16:02-04:00",
                            "articlebody": "This article first appeared on the Riding the Elephant site.The third anniversary of Narendra Modi being sworn in as prime minister was celebrated on May 26 with all the bombast that has come..."
                        }
                    ]
                }
            },
            {
                "kind": "customsearch#result",
                "title": "What's Wrong With Modi's Outmoded Idea of India - Bloomberg",
                "htmlTitle": "What&#39;s Wrong With <b>Modi&#39;s</b> Outmoded Idea of India - Bloomberg",
                "link": "https://www.bloomberg.com/view/articles/2017-05-23/what-s-wrong-with-modi-s-outmoded-idea-of-india",
                "displayLink": "www.bloomberg.com",
                "snippet": "May 23, 2017 ... Three years after he was elected, Prime Minister Narendra Modi looms over \nIndia's political scene like no other leader in the country's recent ...",
                "htmlSnippet": "May 23, 2017 <b>...</b> Three years after he was elected, Prime Minister Narendra <b>Modi</b> looms over <br>\nIndia&#39;s political scene like no other leader in the country&#39;s recent&nbsp;...",
                "cacheId": "AM77FArZGqkJ",
                "formattedUrl": "https://www.bloomberg.com/.../what-s-wrong-with-modi-s-outmoded-idea-of -india",
                "htmlFormattedUrl": "https://www.bloomberg.com/.../what-s-wrong-with-<b>modi</b>-s-outmoded-idea-of -india",
                "pagemap": {
                    "hcard": [
                        {
                            "fn": "Pankaj Mishra",
                            "url": "bbg://people/profile/17261207"
                        },
                        {
                            "fn": "Nisid Hajari",
                            "url": "bbg://people/profile/18002218"
                        }
                    ],
                    "cse_thumbnail": [
                        {
                            "width": "256",
                            "height": "197",
                            "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRHFqLxtA6QfxS1ty7oQwjb52f0yIdwb4qviNj1sCbPt74cWOMB3PCQz0mV"
                        }
                    ],
                    "person": [
                        {
                            "url": "bbg://people/profile/17261207",
                            "name": "Pankaj Mishra"
                        },
                        {
                            "url": "bbg://people/profile/18002218",
                            "name": "Nisid Hajari"
                        }
                    ],
                    "metatags": [
                        {
                            "viewport": "width=device-width,initial-scale=1",
                            "referrer": "unsafe-url",
                            "og:description": "The East Asian strongman model isn’t suited to a diverse country.",
                            "og:image": "https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iA9iBRtzvZ1Q/v0/1200x920.jpg",
                            "og:site_name": "Bloomberg.com",
                            "og:title": "Modi’s Idea of India",
                            "og:type": "article",
                            "og:url": "https://www.bloomberg.com/view/articles/2017-05-23/what-s-wrong-with-modi-s-outmoded-idea-of-india",
                            "fb:status": "Three years on, Modi's vision is becoming darker.",
                            "twitter:card": "summary",
                            "twitter:description": "The East Asian strongman model isn’t suited to a diverse country.",
                            "twitter:image": "https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iA9iBRtzvZ1Q/v0/1200x920.jpg",
                            "twitter:site": "@bv",
                            "twitter:title": "Modi’s Idea of India",
                            "parsely-title": "What's Wrong With Modi's Outmoded Idea of India",
                            "parsely-link": "https://www.bloomberg.com/view/articles/2017-05-23/what-s-wrong-with-modi-s-outmoded-idea-of-india",
                            "parsely-type": "post",
                            "parsely-image-url": "https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iA9iBRtzvZ1Q/v0/1200x920.jpg",
                            "parsely-pub-date": "2017-05-23T21:00:13.706Z",
                            "parsely-section": "view",
                            "parsely-tags": "Narendra Damodardas Modi,India,Asia,Economic Development,Jobs,Military,Pakistan,Monetary Policy,Elections,Muslim,,Region: Global,Page: article",
                            "parsely-post-id": "OQFBOD6S972R01",
                            "parsely-author": "Pankaj Mishra",
                            "apple-mobile-web-app-capable": "no",
                            "apple-mobile-web-app-status-bar-style": "black",
                            "apple-itunes-app": "app-id=281941097, affiliate-data=ct=smartbanner_mobileweb&pt=8949",
                            "sailthru.title": "Modi's Idea of India",
                            "sailthru.author": "Pankaj Mishra",
                            "sailthru.description": "The East Asian strongman model isn’t suited to a diverse country.",
                            "sailthru.date": "2017-05-23T21:00:13.706Z"
                        }
                    ],
                    "cse_image": [
                        {
                            "src": "https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iA9iBRtzvZ1Q/v0/1200x920.jpg"
                        }
                    ],
                    "article": [
                        {
                            "datepublished": "2017-05-23T21:00:13.706Z"
                        }
                    ]
                }
            },
            {
                "kind": "customsearch#result",
                "title": "MODI: Create Anything You Want with Robotics of Things by ...",
                "htmlTitle": "<b>MODI</b>: Create Anything You Want with Robotics of Things by ...",
                "link": "https://www.kickstarter.com/projects/luxrobo/modi-create-anything-you-want-with-robotics-of-thi",
                "displayLink": "www.kickstarter.com",
                "snippet": "Oct 14, 2016 ... When you turn the app on, it searches for MODI Network modules and connects \nautomatically. You can enable and disable the Bluetooth ...",
                "htmlSnippet": "Oct 14, 2016 <b>...</b> When you turn the app on, it searches for <b>MODI</b> Network modules and connects <br>\nautomatically. You can enable and disable the Bluetooth&nbsp;...",
                "cacheId": "QGsrXySVJ8AJ",
                "formattedUrl": "https://www.kickstarter.com/.../modi-create-anything-you-want-with-robotics -of-thi",
                "htmlFormattedUrl": "https://www.kickstarter.com/.../<b>modi</b>-create-anything-you-want-with-robotics -of-thi",
                "pagemap": {
                    "cse_thumbnail": [
                        {
                            "width": "300",
                            "height": "168",
                            "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcR1z3dXONt5Ee4EIzbL9UAgrkzIn7-Gyqe8ObJmB2O9uloKA1slC69meZc"
                        }
                    ],
                    "metatags": [
                        {
                            "format-detection": "telephone=no",
                            "p:domain_verify": "4c4c9100f4bbd16f5f821211782cff9f",
                            "viewport": "width=device-width,initial-scale=1",
                            "title": "Kickstarter >> MODI: Create Anything You Want with Robotics of Things by Luxrobo",
                            "og:title": "MODI: Create Anything You Want with Robotics of Things",
                            "og:type": "kickstarter:project",
                            "og:image": "https://ksr-ugc.imgix.net/assets/013/983/272/5f65c1d126b84b0bad688369225e3510_original.png?w=1552&h=873&fit=fill&bg=000000&v=1478171395&auto=format&q=92&s=c8295ea8f507468e38f3ac3f6124ba22",
                            "og:image:width": "1536",
                            "og:image:height": "1152",
                            "og:url": "https://www.kickstarter.com/projects/luxrobo/modi-create-anything-you-want-with-robotics-of-thi",
                            "og:site_name": "Kickstarter",
                            "fb:app_id": "69103156693",
                            "og:description": "MODI is a modular device for DIY IoT, and robotic creations. Just Connect and Build with MODI module.",
                            "og:locale": "en_US",
                            "og:locale:alternate": "en_US",
                            "kickstarter:creator": "https://www.kickstarter.com/profile/luxrobo",
                            "twitter:card": "summary_large_image",
                            "twitter:site": "@kickstarter",
                            "twitter:site:id": "16186995",
                            "twitter:title": "MODI: Create Anything You Want with Robotics of Things",
                            "twitter:description": "MODI is a modular device for DIY IoT, and robotic creations. Just Connect and Build with MODI module.",
                            "twitter:image": "https://ksr-ugc.imgix.net/assets/013/983/272/5f65c1d126b84b0bad688369225e3510_original.png?w=1024&h=576&fit=fill&bg=000000&v=1478171395&auto=format&q=92&s=51d13989bb678220e6d2f241d891ab08",
                            "twitter:url": "https://www.kickstarter.com/projects/luxrobo/modi-create-anything-you-want-with-robotics-of-thi",
                            "twitter:app:id:iphone": "596961532",
                            "twitter:app:name:iphone": "Kickstarter",
                            "twitter:app:url:iphone": "ksr://www.kickstarter.com/projects/1744087854/1727747614?app_banner=1",
                            "twitter:maxage": "60",
                            "csrf-param": "authenticity_token",
                            "csrf-token": "ZBWw89HsFKC4ZJDoM1cXFRmJ7USlv4NWIiZqk0TRGCSvOIdRd0+M2xwIuACBZH39ZQDujkkqiVXyFeCvDG4Urw=="
                        }
                    ],
                    "cse_image": [
                        {
                            "src": "https://ksr-ugc.imgix.net/assets/013/983/272/5f65c1d126b84b0bad688369225e3510_original.png?w=1552&h=873&fit=fill&bg=000000&v=1478171395&auto=format&q=92&s=c8295ea8f507468e38f3ac3f6124ba22"
                        }
                    ]
                }
            },
            {
                "kind": "customsearch#result",
                "title": "Narendra Modi by Pankaj Mishra: TIME 100 | Time.com",
                "htmlTitle": "Narendra <b>Modi</b> by Pankaj Mishra: TIME 100 | Time.com",
                "link": "http://time.com/collection/2017-time-100/4736335/narendra-modi/",
                "displayLink": "time.com",
                "snippet": "Narendra Modi is on the TIME 100 2017 list. Pankaj Mishra wrote about the \nPrime Minister of India.",
                "htmlSnippet": "Narendra <b>Modi</b> is on the TIME 100 2017 list. Pankaj Mishra wrote about the <br>\nPrime Minister of India.",
                "formattedUrl": "time.com/collection/2017-time-100/4736335/narendra-modi/",
                "htmlFormattedUrl": "time.com/collection/2017-time-100/4736335/narendra-<b>modi</b>/",
                "pagemap": {
                    "cse_thumbnail": [
                        {
                            "width": "195",
                            "height": "259",
                            "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR7Y7UItznBlyewz9F_FPvfXy2SqVBxnjhWizP2ajvtt3VVP6eFr-V5B-Y"
                        }
                    ],
                    "metatags": [
                        {
                            "viewport": "width=device-width, initial-scale=1",
                            "news_keywords": "time 100, time 100 winners, time 100 list, who is on the time 100, narendra modi, narendra modi time 100, narendra modi india, prime minister narendra modi, pm nardendra modi, narendra modi influence",
                            "og:site_name": "Time",
                            "og:type": "article",
                            "og:locale": "en_US",
                            "fb:app_id": "53177223193",
                            "og:title": "Narendra Modi: The World’s 100 Most Influential People",
                            "og:description": "India's undimmed nationalist",
                            "og:url": "http://time.com/collection/2017-time-100/4736335/narendra-modi/",
                            "og:image": "https://timedotcom.files.wordpress.com/2017/04/time-100-2017-narendra-modi.jpg?w=720",
                            "twitter:site": "@TIME",
                            "twitter:title": "Narendra Modi is on @TIME's list of the world's most influential people #TIME100",
                            "twitter:description": "India's undimmed nationalist",
                            "twitter:card": "summary_large_image"
                        }
                    ],
                    "cse_image": [
                        {
                            "src": "https://timedotcom.files.wordpress.com/2017/04/time-100-2017-narendra-modi.jpg?w=720"
                        }
                    ]
                }
            }
        ]
    }
    '''


def image_me_api(search_query):
    base_url = os.environ.get('IMAGE_URL')
    params = {'key': GOOGLE_IMAGE_API_KEY, 'cx': IMAGE_SEARCH_ENGINE_ID, 'q': search_query}
    url_query = parse.urlencode(params)
    google_resp = request.urlopen(base_url + "?%s" % url_query)
    resp_raw = google_resp.read().decode()
    resp = json.loads(resp_raw)
    if resp and "items" in resp:
        result_len = len(resp['items'])
        for i in range(result_len):
            item_index = randrange(result_len)
            try:
                image_link = resp['items'][item_index]["pagemap"]["cse_image"][0]["src"]
                return "here is the image for " + search_query + " as you requested \n <" + image_link + ">"
            except Exception as e:
                print(e)
    else:
        return "Wow! Even Google doesn't have answers for such a dumb " \
               "question, where does these come from! :dizzy_face:"
