from bot_box.features import os, request, parse, json, randrange

from bot_box.bot_constants import BOT_CREATER, USER_AGENT

GIF_API_KEY = os.environ.get('GIF_API_KEY')

''' api.giphy sample response

    {
        "pagination": {
            "offset": 0,
            "count": 5,
            "total_count": 407
        },
        "meta": {
            "response_id": "59462213be45949b6fe735e9",
            "msg": "OK",
            "status": 200
        },
        "data": [
            {
                "source": "http://imgur.com/gallery/ObTeZ27",
                "source_tld": "imgur.com",
                "rating": "g",
                "type": "gif",
                "url": "https://giphy.com/gifs/PJlTNlIND0Ryw",
                "import_datetime": "2016-06-30 03:37:20",
                "is_indexable": 0,
                "content_url": "",
                "source_post_url": "http://imgur.com/gallery/ObTeZ27",
                "bitly_gif_url": "http://gph.is/29ch9TF",
                "slug": "PJlTNlIND0Ryw",
                "id": "PJlTNlIND0Ryw",
                "username": "",
                "trending_datetime": "1970-01-01 00:00:00",
                "bitly_url": "http://gph.is/29ch9TF",
                "embed_url": "https://giphy.com/embed/PJlTNlIND0Ryw",
                "images": {
                    "original_mp4": {
                        "mp4": "https://media4.giphy.com/media/PJlTNlIND0Ryw/giphy.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "353155",
                        "height": "852",
                        "width": "480"s
                    },
                    "downsized_large": {
                        "width": "200",
                        "size": "1839570",
                        "height": "355",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/giphy.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "downsized": {
                        "width": "200",
                        "size": "1839570",
                        "height": "355",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/giphy.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "preview_webp": {
                        "width": "200",
                        "size": "30926",
                        "height": "355",
                        "url": "https://media4.giphy.com/media/PJlTNlIND0Ryw/giphy-preview.webp?response_id=59462213be45949b6fe735e9"
                    },
                    "preview": {
                        "mp4": "https://media4.giphy.com/media/PJlTNlIND0Ryw/giphy-preview.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "37283",
                        "height": "354",
                        "width": "200"
                    },
                    "fixed_width_small_still": {
                        "width": "100",
                        "height": "178",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/100w_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_height_still": {
                        "width": "113",
                        "height": "200",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/200_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_height_small": {
                        "mp4": "https://media4.giphy.com/media/PJlTNlIND0Ryw/100.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "13086",
                        "webp_size": "66530",
                        "size": "137447",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/100.gif?response_id=59462213be45949b6fe735e9",
                        "width": "56",
                        "webp": "https://media3.giphy.com/media/PJlTNlIND0Ryw/100.webp?response_id=59462213be45949b6fe735e9",
                        "height": "100"
                    },
                    "downsized_still": {
                        "width": "200",
                        "height": "355",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/giphy_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_width_still": {
                        "width": "200",
                        "height": "355",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/200w_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_width_small": {
                        "mp4": "https://media4.giphy.com/media/PJlTNlIND0Ryw/100w.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "30062",
                        "webp_size": "170048",
                        "size": "427580",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/100w.gif?response_id=59462213be45949b6fe735e9",
                        "width": "100",
                        "webp": "https://media3.giphy.com/media/PJlTNlIND0Ryw/100w.webp?response_id=59462213be45949b6fe735e9",
                        "height": "178"
                    },
                    "original": {
                        "mp4": "https://media3.giphy.com/media/PJlTNlIND0Ryw/giphy.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "353155",
                        "webp_size": "520864",
                        "size": "1839570",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/giphy.gif?response_id=59462213be45949b6fe735e9",
                        "width": "200",
                        "frames": "61",
                        "webp": "https://media3.giphy.com/media/PJlTNlIND0Ryw/giphy.webp?response_id=59462213be45949b6fe735e9",
                        "height": "355"
                    },
                    "preview_gif": {
                        "width": "112",
                        "size": "49611",
                        "height": "199",
                        "url": "https://media4.giphy.com/media/PJlTNlIND0Ryw/giphy-preview.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "looping": {
                        "mp4": "https://media4.giphy.com/media/PJlTNlIND0Ryw/giphy-loop.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "518845"
                    },
                    "original_still": {
                        "width": "200",
                        "height": "355",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/giphy_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_height_downsampled": {
                        "webp_size": "19470",
                        "size": "52952",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/200_d.gif?response_id=59462213be45949b6fe735e9",
                        "width": "113",
                        "webp": "https://media3.giphy.com/media/PJlTNlIND0Ryw/200_d.webp?response_id=59462213be45949b6fe735e9",
                        "height": "200"
                    },
                    "fixed_width": {
                        "mp4": "https://media4.giphy.com/media/PJlTNlIND0Ryw/200w.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "82374",
                        "webp_size": "520864",
                        "size": "1841436",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/200w.gif?response_id=59462213be45949b6fe735e9",
                        "width": "200",
                        "webp": "https://media3.giphy.com/media/PJlTNlIND0Ryw/200w.webp?response_id=59462213be45949b6fe735e9",
                        "height": "355"
                    },
                    "fixed_width_downsampled": {
                        "webp_size": "50666",
                        "size": "171144",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/200w_d.gif?response_id=59462213be45949b6fe735e9",
                        "width": "200",
                        "webp": "https://media3.giphy.com/media/PJlTNlIND0Ryw/200w_d.webp?response_id=59462213be45949b6fe735e9",
                        "height": "355"
                    },
                    "fixed_height_small_still": {
                        "width": "56",
                        "height": "100",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/100_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "downsized_medium": {
                        "width": "200",
                        "size": "1839570",
                        "height": "355",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/giphy.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "downsized_small": {
                        "mp4": "https://media4.giphy.com/media/PJlTNlIND0Ryw/giphy-downsized-small.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "108692",
                        "height": "354",
                        "width": "200"
                    },
                    "fixed_height": {
                        "mp4": "https://media4.giphy.com/media/PJlTNlIND0Ryw/200.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "35605",
                        "webp_size": "195518",
                        "size": "542565",
                        "url": "https://media3.giphy.com/media/PJlTNlIND0Ryw/200.gif?response_id=59462213be45949b6fe735e9",
                        "width": "113",
                        "webp": "https://media3.giphy.com/media/PJlTNlIND0Ryw/200.webp?response_id=59462213be45949b6fe735e9",
                        "height": "200"
                    }
                }
            },
            {
                "source": "http://imgur.com/gallery/giO7i84",
                "source_tld": "imgur.com",
                "rating": "g",
                "type": "gif",
                "url": "https://giphy.com/gifs/11nCYa0XqPKa2s",
                "import_datetime": "2016-06-25 12:44:00",
                "is_indexable": 0,
                "content_url": "",
                "source_post_url": "http://imgur.com/gallery/giO7i84",
                "bitly_gif_url": "http://gph.is/28YwN6G",
                "slug": "11nCYa0XqPKa2s",
                "id": "11nCYa0XqPKa2s",
                "username": "",
                "trending_datetime": "1970-01-01 00:00:00",
                "bitly_url": "http://gph.is/28YwN6G",
                "embed_url": "https://giphy.com/embed/11nCYa0XqPKa2s",
                "images": {
                    "original_mp4": {
                        "mp4": "https://media4.giphy.com/media/11nCYa0XqPKa2s/giphy.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "94938",
                        "height": "200",
                        "width": "480"
                    },
                    "downsized_large": {
                        "width": "720",
                        "size": "3931824",
                        "height": "300",
                        "url": "https://media2.giphy.com/media/11nCYa0XqPKa2s/giphy.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "downsized": {
                        "width": "500",
                        "size": "1821642",
                        "height": "208",
                        "url": "https://media4.giphy.com/media/11nCYa0XqPKa2s/giphy-downsized.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "preview_webp": {
                        "width": "302",
                        "size": "49368",
                        "height": "126",
                        "url": "https://media4.giphy.com/media/11nCYa0XqPKa2s/giphy-preview.webp?response_id=59462213be45949b6fe735e9"
                    },
                    "preview": {
                        "mp4": "https://media4.giphy.com/media/11nCYa0XqPKa2s/giphy-preview.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "46822",
                        "height": "190",
                        "width": "456"
                    },
                    "fixed_width_small_still": {
                        "width": "100",
                        "height": "42",
                        "url": "https://media2.giphy.com/media/11nCYa0XqPKa2s/100w_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_height_still": {
                        "width": "480",
                        "height": "200",
                        "url": "https://media2.giphy.com/media/11nCYa0XqPKa2s/200_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_height_small": {
                        "mp4": "https://media4.giphy.com/media/11nCYa0XqPKa2s/100.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "32887",
                        "webp_size": "153054",
                        "size": "478206",
                        "url": "https://media2.giphy.com/media/11nCYa0XqPKa2s/100.gif?response_id=59462213be45949b6fe735e9",
                        "width": "240",
                        "webp": "https://media2.giphy.com/media/11nCYa0XqPKa2s/100.webp?response_id=59462213be45949b6fe735e9",
                        "height": "100"
                    },
                    "downsized_still": {
                        "width": "500",
                        "size": "51910",
                        "height": "208",
                        "url": "https://media4.giphy.com/media/11nCYa0XqPKa2s/giphy-downsized_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_width_still": {
                        "width": "200",
                        "height": "83",
                        "url": "https://media2.giphy.com/media/11nCYa0XqPKa2s/200w_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_width_small": {
                        "mp4": "https://media4.giphy.com/media/11nCYa0XqPKa2s/100w.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "10487",
                        "webp_size": "44544",
                        "size": "91370",
                        "url": "https://media2.giphy.com/media/11nCYa0XqPKa2s/100w.gif?response_id=59462213be45949b6fe735e9",
                        "width": "100",
                        "webp": "https://media2.giphy.com/media/11nCYa0XqPKa2s/100w.webp?response_id=59462213be45949b6fe735e9",
                        "height": "42"
                    },
                    "original": {
                        "mp4": "https://media2.giphy.com/media/11nCYa0XqPKa2s/giphy.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "94938",
                        "webp_size": "736464",
                        "size": "3931824",
                        "url": "https://media2.giphy.com/media/11nCYa0XqPKa2s/giphy.gif?response_id=59462213be45949b6fe735e9",
                        "width": "720",
                        "frames": "36",
                        "webp": "https://media2.giphy.com/media/11nCYa0XqPKa2s/giphy.webp?response_id=59462213be45949b6fe735e9",
                        "height": "300"
                    },
                    "preview_gif": {
                        "width": "161",
                        "size": "49827",
                        "height": "67",
                        "url": "https://media4.giphy.com/media/11nCYa0XqPKa2s/giphy-preview.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "looping": {
                        "mp4": "https://media4.giphy.com/media/11nCYa0XqPKa2s/giphy-loop.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "408984"
                    },
                    "original_still": {
                        "width": "720",
                        "height": "300",
                        "url": "https://media2.giphy.com/media/11nCYa0XqPKa2s/giphy_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_height_downsampled": {
                        "webp_size": "68946",
                        "size": "281051",
                        "url": "https://media2.giphy.com/media/11nCYa0XqPKa2s/200_d.gif?response_id=59462213be45949b6fe735e9",
                        "width": "480",
                        "webp": "https://media2.giphy.com/media/11nCYa0XqPKa2s/200_d.webp?response_id=59462213be45949b6fe735e9",
                        "height": "200"
                    },
                    "fixed_width": {
                        "mp4": "https://media4.giphy.com/media/11nCYa0XqPKa2s/200w.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "27534",
                        "webp_size": "115186",
                        "size": "309181",
                        "url": "https://media2.giphy.com/media/11nCYa0XqPKa2s/200w.gif?response_id=59462213be45949b6fe735e9",
                        "width": "200",
                        "webp": "https://media2.giphy.com/media/11nCYa0XqPKa2s/200w.webp?response_id=59462213be45949b6fe735e9",
                        "height": "83"
                    },
                    "fixed_width_downsampled": {
                        "webp_size": "19104",
                        "size": "53543",
                        "url": "https://media2.giphy.com/media/11nCYa0XqPKa2s/200w_d.gif?response_id=59462213be45949b6fe735e9",
                        "width": "200",
                        "webp": "https://media2.giphy.com/media/11nCYa0XqPKa2s/200w_d.webp?response_id=59462213be45949b6fe735e9",
                        "height": "83"
                    },
                    "fixed_height_small_still": {
                        "width": "240",
                        "height": "100",
                        "url": "https://media2.giphy.com/media/11nCYa0XqPKa2s/100_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "downsized_medium": {
                        "width": "720",
                        "size": "3931824",
                        "height": "300",
                        "url": "https://media2.giphy.com/media/11nCYa0XqPKa2s/giphy.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "downsized_small": {
                        "mp4": "https://media4.giphy.com/media/11nCYa0XqPKa2s/giphy-downsized-small.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "179266",
                        "height": "264",
                        "width": "633"
                    },
                    "fixed_height": {
                        "mp4": "https://media4.giphy.com/media/11nCYa0XqPKa2s/200.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "84241",
                        "webp_size": "414774",
                        "size": "1665442",
                        "url": "https://media2.giphy.com/media/11nCYa0XqPKa2s/200.gif?response_id=59462213be45949b6fe735e9",
                        "width": "480",
                        "webp": "https://media2.giphy.com/media/11nCYa0XqPKa2s/200.webp?response_id=59462213be45949b6fe735e9",
                        "height": "200"
                    }
                }
            },
            {
                "source": "http://imgur.com/gallery/wGHigHt",
                "source_tld": "imgur.com",
                "rating": "pg",
                "type": "gif",
                "url": "https://giphy.com/gifs/VAJfmbXAIBu0M",
                "import_datetime": "2016-06-22 03:13:02",
                "is_indexable": 0,
                "content_url": "",
                "source_post_url": "http://imgur.com/gallery/wGHigHt",
                "bitly_gif_url": "http://gph.is/28Msc6T",
                "slug": "VAJfmbXAIBu0M",
                "id": "VAJfmbXAIBu0M",
                "username": "",
                "trending_datetime": "1970-01-01 00:00:00",
                "bitly_url": "http://gph.is/28Msc6T",
                "embed_url": "https://giphy.com/embed/VAJfmbXAIBu0M",
                "images": {
                    "original_mp4": {
                        "mp4": "https://media2.giphy.com/media/VAJfmbXAIBu0M/giphy.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "160853",
                        "height": "258",
                        "width": "480"
                    },
                    "downsized_large": {
                        "width": "500",
                        "size": "2242012",
                        "height": "270",
                        "url": "https://media0.giphy.com/media/VAJfmbXAIBu0M/giphy.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "downsized": {
                        "width": "250",
                        "size": "704822",
                        "height": "135",
                        "url": "https://media2.giphy.com/media/VAJfmbXAIBu0M/giphy-downsized.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "preview_webp": {
                        "width": "193",
                        "size": "48716",
                        "height": "104",
                        "url": "https://media2.giphy.com/media/VAJfmbXAIBu0M/giphy-preview.webp?response_id=59462213be45949b6fe735e9"
                    },
                    "preview": {
                        "mp4": "https://media2.giphy.com/media/VAJfmbXAIBu0M/giphy-preview.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "36938",
                        "height": "132",
                        "width": "246"
                    },
                    "fixed_width_small_still": {
                        "width": "100",
                        "height": "54",
                        "url": "https://media0.giphy.com/media/VAJfmbXAIBu0M/100w_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_height_still": {
                        "width": "370",
                        "height": "200",
                        "url": "https://media0.giphy.com/media/VAJfmbXAIBu0M/200_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_height_small": {
                        "mp4": "https://media2.giphy.com/media/VAJfmbXAIBu0M/100.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "29982",
                        "webp_size": "152130",
                        "size": "421514",
                        "url": "https://media0.giphy.com/media/VAJfmbXAIBu0M/100.gif?response_id=59462213be45949b6fe735e9",
                        "width": "185",
                        "webp": "https://media0.giphy.com/media/VAJfmbXAIBu0M/100.webp?response_id=59462213be45949b6fe735e9",
                        "height": "100"
                    },
                    "downsized_still": {
                        "width": "250",
                        "size": "23298",
                        "height": "135",
                        "url": "https://media2.giphy.com/media/VAJfmbXAIBu0M/giphy-downsized_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_width_still": {
                        "width": "200",
                        "height": "108",
                        "url": "https://media0.giphy.com/media/VAJfmbXAIBu0M/200w_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_width_small": {
                        "mp4": "https://media2.giphy.com/media/VAJfmbXAIBu0M/100w.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "12921",
                        "webp_size": "63770",
                        "size": "157119",
                        "url": "https://media0.giphy.com/media/VAJfmbXAIBu0M/100w.gif?response_id=59462213be45949b6fe735e9",
                        "width": "100",
                        "webp": "https://media0.giphy.com/media/VAJfmbXAIBu0M/100w.webp?response_id=59462213be45949b6fe735e9",
                        "height": "54"
                    },
                    "original": {
                        "mp4": "https://media0.giphy.com/media/VAJfmbXAIBu0M/giphy.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "160853",
                        "webp_size": "670310",
                        "size": "2242012",
                        "url": "https://media0.giphy.com/media/VAJfmbXAIBu0M/giphy.gif?response_id=59462213be45949b6fe735e9",
                        "width": "500",
                        "frames": "31",
                        "webp": "https://media0.giphy.com/media/VAJfmbXAIBu0M/giphy.webp?response_id=59462213be45949b6fe735e9",
                        "height": "270"
                    },
                    "preview_gif": {
                        "width": "122",
                        "size": "48626",
                        "height": "66",
                        "url": "https://media2.giphy.com/media/VAJfmbXAIBu0M/giphy-preview.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "looping": {
                        "mp4": "https://media2.giphy.com/media/VAJfmbXAIBu0M/giphy-loop.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "842563"
                    },
                    "original_still": {
                        "width": "500",
                        "height": "270",
                        "url": "https://media0.giphy.com/media/VAJfmbXAIBu0M/giphy_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_height_downsampled": {
                        "webp_size": "80654",
                        "size": "265121",
                        "url": "https://media0.giphy.com/media/VAJfmbXAIBu0M/200_d.gif?response_id=59462213be45949b6fe735e9",
                        "width": "370",
                        "webp": "https://media0.giphy.com/media/VAJfmbXAIBu0M/200_d.webp?response_id=59462213be45949b6fe735e9",
                        "height": "200"
                    },
                    "fixed_width": {
                        "mp4": "https://media2.giphy.com/media/VAJfmbXAIBu0M/200w.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "35709",
                        "webp_size": "168788",
                        "size": "474118",
                        "url": "https://media0.giphy.com/media/VAJfmbXAIBu0M/200w.gif?response_id=59462213be45949b6fe735e9",
                        "width": "200",
                        "webp": "https://media0.giphy.com/media/VAJfmbXAIBu0M/200w.webp?response_id=59462213be45949b6fe735e9",
                        "height": "108"
                    },
                    "fixed_width_downsampled": {
                        "webp_size": "33128",
                        "size": "91815",
                        "url": "https://media0.giphy.com/media/VAJfmbXAIBu0M/200w_d.gif?response_id=59462213be45949b6fe735e9",
                        "width": "200",
                        "webp": "https://media0.giphy.com/media/VAJfmbXAIBu0M/200w_d.webp?response_id=59462213be45949b6fe735e9",
                        "height": "108"
                    },
                    "fixed_height_small_still": {
                        "width": "185",
                        "height": "100",
                        "url": "https://media0.giphy.com/media/VAJfmbXAIBu0M/100_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "downsized_medium": {
                        "width": "500",
                        "size": "2242012",
                        "height": "270",
                        "url": "https://media0.giphy.com/media/VAJfmbXAIBu0M/giphy.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "downsized_small": {
                        "mp4": "https://media2.giphy.com/media/VAJfmbXAIBu0M/giphy-downsized-small.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "160632",
                        "height": "242",
                        "width": "448"
                    },
                    "fixed_height": {
                        "mp4": "https://media2.giphy.com/media/VAJfmbXAIBu0M/200.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "90772",
                        "webp_size": "410428",
                        "size": "1334694",
                        "url": "https://media0.giphy.com/media/VAJfmbXAIBu0M/200.gif?response_id=59462213be45949b6fe735e9",
                        "width": "370",
                        "webp": "https://media0.giphy.com/media/VAJfmbXAIBu0M/200.webp?response_id=59462213be45949b6fe735e9",
                        "height": "200"
                    }
                }
            },
            {
                "source": "https://www.buzzfeed.com/joeloliphint/anna-jarvis-was-sorry-she-ever-invented-mothers-day",
                "source_tld": "www.buzzfeed.com",
                "rating": "g",
                "type": "gif",
                "url": "https://giphy.com/gifs/news-buzzfeed-mothers-gwtp3vsTt2zkY",
                "import_datetime": "2017-01-26 20:06:41",
                "is_indexable": 0,
                "content_url": "",
                "source_post_url": "https://www.buzzfeed.com/joeloliphint/anna-jarvis-was-sorry-she-ever-invented-mothers-day",
                "bitly_gif_url": "http://gph.is/2k6nCVx",
                "slug": "news-buzzfeed-mothers-gwtp3vsTt2zkY",
                "id": "gwtp3vsTt2zkY",
                "username": "",
                "trending_datetime": "0000-00-00 00:00:00",
                "bitly_url": "http://gph.is/2k6nCVx",
                "embed_url": "https://giphy.com/embed/gwtp3vsTt2zkY",
                "images": {
                    "original_mp4": {
                        "mp4": "https://media3.giphy.com/media/gwtp3vsTt2zkY/giphy.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "133204",
                        "height": "270",
                        "width": "480"
                    },
                    "downsized_large": {
                        "width": "480",
                        "size": "938226",
                        "height": "270",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/giphy.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "downsized": {
                        "width": "480",
                        "size": "938226",
                        "height": "270",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/giphy-downsized.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "preview_webp": {
                        "width": "480",
                        "size": "22044",
                        "height": "270",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/giphy-preview.webp?response_id=59462213be45949b6fe735e9"
                    },
                    "preview": {
                        "mp4": "https://media3.giphy.com/media/gwtp3vsTt2zkY/giphy-preview.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "37718",
                        "height": "216",
                        "width": "384"
                    },
                    "fixed_width_small_still": {
                        "width": "100",
                        "size": "5406",
                        "height": "57",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/100w_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_height_still": {
                        "width": "356",
                        "size": "45803",
                        "height": "200",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/200_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_height_small": {
                        "mp4": "https://media3.giphy.com/media/gwtp3vsTt2zkY/100.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "11650",
                        "webp_size": "43878",
                        "size": "124877",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/100.gif?response_id=59462213be45949b6fe735e9",
                        "width": "178",
                        "webp": "https://media3.giphy.com/media/gwtp3vsTt2zkY/100.webp?response_id=59462213be45949b6fe735e9",
                        "height": "100"
                    },
                    "downsized_still": {
                        "width": "480",
                        "size": "82495",
                        "height": "270",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/giphy-downsized_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_width_still": {
                        "width": "200",
                        "size": "16375",
                        "height": "113",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/200w_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_width_small": {
                        "mp4": "https://media3.giphy.com/media/gwtp3vsTt2zkY/100w.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "5177",
                        "webp_size": "16464",
                        "size": "45032",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/100w.gif?response_id=59462213be45949b6fe735e9",
                        "width": "100",
                        "webp": "https://media3.giphy.com/media/gwtp3vsTt2zkY/100w.webp?response_id=59462213be45949b6fe735e9",
                        "height": "57"
                    },
                    "original": {
                        "mp4": "https://media2.giphy.com/media/gwtp3vsTt2zkY/giphy.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "133204",
                        "webp_size": "253716",
                        "size": "938226",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/giphy.gif?response_id=59462213be45949b6fe735e9",
                        "hash": "b3e829bb5dfdd6993cdcf150d59eb8df",
                        "width": "480",
                        "frames": "11",
                        "webp": "https://media3.giphy.com/media/gwtp3vsTt2zkY/giphy.webp?response_id=59462213be45949b6fe735e9",
                        "height": "270"
                    },
                    "preview_gif": {
                        "width": "400",
                        "size": "47990",
                        "height": "225",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/giphy-preview.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "looping": {
                        "mp4": "https://media3.giphy.com/media/gwtp3vsTt2zkY/giphy-loop.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "429826"
                    },
                    "original_still": {
                        "width": "480",
                        "size": "82495",
                        "height": "270",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/giphy_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_height_downsampled": {
                        "webp_size": "77548",
                        "size": "233867",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/200_d.gif?response_id=59462213be45949b6fe735e9",
                        "width": "356",
                        "webp": "https://media3.giphy.com/media/gwtp3vsTt2zkY/200_d.webp?response_id=59462213be45949b6fe735e9",
                        "height": "200"
                    },
                    "hd": {
                        "mp4": "https://media3.giphy.com/media/gwtp3vsTt2zkY/giphy-hd.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "648112",
                        "height": "556",
                        "width": "990"
                    },
                    "fixed_width": {
                        "mp4": "https://media3.giphy.com/media/gwtp3vsTt2zkY/200w.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "14217",
                        "webp_size": "53324",
                        "size": "146271",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/200w.gif?response_id=59462213be45949b6fe735e9",
                        "width": "200",
                        "webp": "https://media3.giphy.com/media/gwtp3vsTt2zkY/200w.webp?response_id=59462213be45949b6fe735e9",
                        "height": "113"
                    },
                    "fixed_width_downsampled": {
                        "webp_size": "29788",
                        "size": "70029",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/200w_d.gif?response_id=59462213be45949b6fe735e9",
                        "width": "200",
                        "webp": "https://media3.giphy.com/media/gwtp3vsTt2zkY/200w_d.webp?response_id=59462213be45949b6fe735e9",
                        "height": "113"
                    },
                    "fixed_height_small_still": {
                        "width": "178",
                        "size": "13439",
                        "height": "100",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/100_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "downsized_medium": {
                        "width": "480",
                        "size": "938226",
                        "height": "270",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/giphy.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "downsized_small": {
                        "mp4": "https://media3.giphy.com/media/gwtp3vsTt2zkY/giphy-downsized-small.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "129444",
                        "height": "270",
                        "width": "480"
                    },
                    "fixed_height": {
                        "mp4": "https://media3.giphy.com/media/gwtp3vsTt2zkY/200.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "45527",
                        "webp_size": "134570",
                        "size": "460819",
                        "url": "https://media3.giphy.com/media/gwtp3vsTt2zkY/200.gif?response_id=59462213be45949b6fe735e9",
                        "width": "356",
                        "webp": "https://media3.giphy.com/media/gwtp3vsTt2zkY/200.webp?response_id=59462213be45949b6fe735e9",
                        "height": "200"
                    }
                }
            },
            {
                "source": "http://imgur.com/gallery/Xs7fbCS",
                "source_tld": "imgur.com",
                "rating": "g",
                "type": "gif",
                "url": "https://giphy.com/gifs/bCHEQYjUj7Ra8",
                "import_datetime": "2016-06-27 05:29:35",
                "is_indexable": 0,
                "content_url": "",
                "source_post_url": "http://imgur.com/gallery/Xs7fbCS",
                "bitly_gif_url": "http://gph.is/28XBJnV",
                "slug": "bCHEQYjUj7Ra8",
                "id": "bCHEQYjUj7Ra8",
                "username": "",
                "trending_datetime": "1970-01-01 00:00:00",
                "bitly_url": "http://gph.is/28XBJnV",
                "embed_url": "https://giphy.com/embed/bCHEQYjUj7Ra8",
                "images": {
                    "original_mp4": {
                        "mp4": "https://media4.giphy.com/media/bCHEQYjUj7Ra8/giphy.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "1579632",
                        "height": "262",
                        "width": "480"
                    },
                    "downsized_large": {
                        "width": "400",
                        "size": "4960689",
                        "height": "220",
                        "url": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/giphy-downsized-large.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "downsized": {
                        "width": "250",
                        "size": "1227119",
                        "height": "137",
                        "url": "https://media4.giphy.com/media/bCHEQYjUj7Ra8/giphy-downsized.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "preview_webp": {
                        "width": "231",
                        "size": "47830",
                        "height": "127",
                        "url": "https://media4.giphy.com/media/bCHEQYjUj7Ra8/giphy-preview.webp?response_id=59462213be45949b6fe735e9"
                    },
                    "preview": {
                        "mp4": "https://media4.giphy.com/media/bCHEQYjUj7Ra8/giphy-preview.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "47413",
                        "height": "164",
                        "width": "300"
                    },
                    "fixed_width_small_still": {
                        "width": "100",
                        "height": "55",
                        "url": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/100w_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_height_still": {
                        "width": "365",
                        "height": "200",
                        "url": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/200_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_height_small": {
                        "mp4": "https://media4.giphy.com/media/bCHEQYjUj7Ra8/100.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "41074",
                        "webp_size": "1296322",
                        "size": "3925435",
                        "url": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/100.gif?response_id=59462213be45949b6fe735e9",
                        "width": "182",
                        "webp": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/100.webp?response_id=59462213be45949b6fe735e9",
                        "height": "100"
                    },
                    "downsized_still": {
                        "width": "250",
                        "size": "16698",
                        "height": "137",
                        "url": "https://media4.giphy.com/media/bCHEQYjUj7Ra8/giphy-downsized_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_width_still": {
                        "width": "200",
                        "height": "110",
                        "url": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/200w_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_width_small": {
                        "mp4": "https://media4.giphy.com/media/bCHEQYjUj7Ra8/100w.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "39415",
                        "webp_size": "571156",
                        "size": "1552713",
                        "url": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/100w.gif?response_id=59462213be45949b6fe735e9",
                        "width": "100",
                        "webp": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/100w.webp?response_id=59462213be45949b6fe735e9",
                        "height": "55"
                    },
                    "original": {
                        "mp4": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/giphy.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "1579632",
                        "webp_size": "9356934",
                        "size": "37201858",
                        "url": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/giphy.gif?response_id=59462213be45949b6fe735e9",
                        "width": "627",
                        "frames": "327",
                        "webp": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/giphy.webp?response_id=59462213be45949b6fe735e9",
                        "height": "344"
                    },
                    "preview_gif": {
                        "width": "149",
                        "size": "48150",
                        "height": "82",
                        "url": "https://media4.giphy.com/media/bCHEQYjUj7Ra8/giphy-preview.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "looping": {
                        "mp4": "https://media4.giphy.com/media/bCHEQYjUj7Ra8/giphy-loop.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "1238388"
                    },
                    "original_still": {
                        "width": "627",
                        "height": "344",
                        "url": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/giphy_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "fixed_height_downsampled": {
                        "webp_size": "132178",
                        "size": "259911",
                        "url": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/200_d.gif?response_id=59462213be45949b6fe735e9",
                        "width": "365",
                        "webp": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/200_d.webp?response_id=59462213be45949b6fe735e9",
                        "height": "200"
                    },
                    "fixed_width": {
                        "mp4": "https://media4.giphy.com/media/bCHEQYjUj7Ra8/200w.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "435624",
                        "webp_size": "1472090",
                        "size": "4547498",
                        "url": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/200w.gif?response_id=59462213be45949b6fe735e9",
                        "width": "200",
                        "webp": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/200w.webp?response_id=59462213be45949b6fe735e9",
                        "height": "110"
                    },
                    "fixed_width_downsampled": {
                        "webp_size": "47838",
                        "size": "86007",
                        "url": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/200w_d.gif?response_id=59462213be45949b6fe735e9",
                        "width": "200",
                        "webp": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/200w_d.webp?response_id=59462213be45949b6fe735e9",
                        "height": "110"
                    },
                    "fixed_height_small_still": {
                        "width": "182",
                        "height": "100",
                        "url": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/100_s.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "downsized_medium": {
                        "width": "364",
                        "size": "3187960",
                        "height": "200",
                        "url": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/giphy-downsized-medium.gif?response_id=59462213be45949b6fe735e9"
                    },
                    "downsized_small": {
                        "mp4": "https://media4.giphy.com/media/bCHEQYjUj7Ra8/giphy-downsized-small.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "161087",
                        "height": "82",
                        "width": "149"
                    },
                    "fixed_height": {
                        "mp4": "https://media4.giphy.com/media/bCHEQYjUj7Ra8/200.mp4?response_id=59462213be45949b6fe735e9",
                        "mp4_size": "1005957",
                        "webp_size": "3526686",
                        "size": "13446400",
                        "url": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/200.gif?response_id=59462213be45949b6fe735e9",
                        "width": "365",
                        "webp": "https://media0.giphy.com/media/bCHEQYjUj7Ra8/200.webp?response_id=59462213be45949b6fe735e9",
                        "height": "200"
                    }
                }
            }
        ]
    }

    '''


def animate_me_api(search_query):
    """
    Result of animate command of user
    :param search_query:
    :return: URL of the gif or else an error message
    """
    size_limit = 3000000
    search_limit = 5
    headers = {'user-agent': USER_AGENT}
    base_url = os.environ.get('ANIMATE_URL')
    params = {'limit': search_limit, 'q': search_query, 'api_key': GIF_API_KEY}
    full_url = base_url + "?%s" % parse.urlencode(params)
    api_req = request.Request(full_url, headers=headers)
    api_call = request.urlopen(api_req)
    response_json = json.loads(api_call.read().decode())
    if response_json and 'data' in response_json:
        resp_len = len(response_json['data'])
        if resp_len > 0:
            resp_index = randrange(resp_len)
            print(resp_index)
            resp_gif_url = response_json['data'][resp_index]['url']
            loop_no = 0
            downsized_resp_gif_url = ""
            while downsized_resp_gif_url == "" and loop_no < search_limit:
                if 'images' in response_json['data'][resp_index]:
                    downsized = response_json['data'][resp_index]['images']['downsized']
                    if int(downsized['size']) < size_limit:
                        downsized_resp_gif_url = downsized['url']
                        print("returning downsized gif")
                        return downsized_resp_gif_url
                loop_no += 1
                resp_index = randrange(resp_len)
            return "<" + resp_gif_url + ">"
        else:  # if no result is found
            return "Sorry, I don't have anything for this nonsense :expressionless:"
    else:
        return (
            "Seems that there is :beetle: in me, Please contact my creater, " + BOT_CREATER +
            ", and ask them to investigate the matter")
