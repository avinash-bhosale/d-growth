# -*- coding: utf-8 -*-

CONTENT_TYPE = "application/json"
SUCCESS_KEY = "success"
ERROR_KEY = "errors"
POST_METHOD = "POST"
GET_METHOD = "GET"
SUCCESS_RES = 'Success'
ERROR_RES = 'Error'
MOBILE_VALIDATION_E = "Expected format: 10 digits of your mobile number without starting with 0 or country code"
NAME_VALIDATION_E = "Must be 1-20 characters and should not contain any number or any special character."


class GeoTypes(object):
    STATE = 'state'
    DISTRICT = 'district'
    TALUKA = 'taluka'
    VILLAGE = 'village'
    # CITY = 'city'
    # COUNTRY = 'country'


user_dict = {
    'password': 'admin123',
    'role': 'Administrator',
    'name': 'Administrator',
    'mobile': '9999999999',
    'email': 'contact@agileinfo.com',
    'gender': 0,
    'address': 'pune',
}
admin_dict = {'name': 'Administrator',
              'email': 'cotact@agileinfo.com',
              'mobile': '9999999999',
              'sex': 0,
              'address': 'pune',
              }


class State(object):
    AP = 'Andhra Pradesh'
    AR = 'Arunachal Pradesh'
    AS = 'Assam'
    BR = 'Bihar'
    CG = 'Chhattisgarh'
    GA = 'Goa'
    GJ = 'Gujarat'
    HR = 'Haryana'
    HP = 'Himachal Pradesh'
    JK = 'Jammu and Kashmir'
    JH = 'Jharkhand'
    KA = 'Karnataka'
    KL = 'Kerala'
    MP = 'Madhya Pradesh'
    MH = 'Maharashtra'
    MN = 'Manipur'
    ML = 'Meghalaya'
    MZ = 'Mizoram'
    NL = 'Nagaland'
    OR = 'Orissa'
    PB = 'Punjab'
    RJ = 'Rajasthan'
    SK = 'Sikkim'
    TN = 'Tamil Nadu'
    TG = 'Telangana'
    TR = 'Tripura'
    UK = 'Uttarakhand'
    UP = 'Uttar Pradesh'
    WB = 'West Bengal'
    AN = 'Andaman and Nicobar Islands'
    CH = 'Chandigarh'
    DH = 'Dadra and Nagar Haveli'
    DD = 'Daman and Diu'
    DL = 'Delhi'
    LD = 'Lakshadweep'
    PY = 'Pondicherry'


geo_dict = {
    State.MH: {
        'Beed': {
            'Beed': ['Adgaon', 'Aher Dhanora', 'Aher Nimgaon', 'Aher wadgaon'],
            'Georai': ['Umapur','Vanjarwadi','Vasatnagar'],
            'Parli': ['Anandwadi', 'Aswalamba', 'Aurangapur'],
            'Ambejogai': ['Akola', 'Ambaltek', 'Apegaon'],
            'Manjlegaon': ['Abegaon', 'Alapur', 'Belura'],
            'Kaij': ['Adas', 'Anandgaon', 'Andhle-Wadi'],
            'Ashti': ['Ambewadi', 'Ambhora', 'Balewadi'],
            'Shirur': ['Alegaon Paga', 'Chandoh', 'Dhanore'],
            'Patoda': ['Amalner', 'Bensur', 'Chumbli'],
            'Dharur': ['Aad-Hingani', 'Asardhav', 'Chatgaon'],
            'Wadwani': ['Devdhi', 'Hiwargavhan', 'Khadki'],
        },
        'Pune': {
            'Pune City': ['Keshavnagar-Mundwa', 'Kirkee Cantonment'],
            'Haveli': ['Bhagatwadi', 'Bhilarewadi', 'Biwari'],
            'Khed': ['Ahire', 'Ambethan'],
            'Baramati': ['Ambi Bk', 'Ambi Kh'],
            'Junnar': ['Amboli', 'Aptale'],
            'Shirur': ['Ganegaon Khalsa', 'Hivare'],
            'Indapur': ['Ajoti', 'Awasari'],
            'Daund': ['Alegaon', 'Boribel'],
            'Mawal': ['Adavi', 'Bedse'],
            'Ambegaon': ['Amade', 'Bharadi'],
            'Purandhar': ['Bopgaon', 'Chambali'],
            'Bhor': ['Dere', 'Dhavadi'],
            'Mulshi': ['Asade', 'Bhare'],
            'Velhe': ['Bhalvadi', 'Chandar'],
        }
    },
    State.RJ: {
        'Ajmer': {
            'Kishangarh': ['Amarpura', 'Bakarwaliya', 'Balapura'],
            'Masuda': ['Bhoodol', 'Bubani', 'Chhatri'],
            'Nasirabad': ['Ashapura', 'Banewara', 'Bhatiyani'],
        },
        'Baran': {
            'Anta': ['Amalsara', 'Bala Khera', 'Baldara', 'Bamooliya Mataji'],
            'Kishanganj': ['Ahmada', 'Akodiya', 'Badipura'],
            'Bikaner': ['Anandpura', 'Bandha', 'Barsingsar'],
        },
    },
}


class Permissions:
    USER_PERMISSION = 1
    DOCTOR_PERMISSION = 2
    PATIENT_PERMISSION = 4
    ORGADMIN_PERMISSION = 8
    ADMIN_PERMISSION = 16


class UserRoles:
    USER = 'User'
    ADMIN = 'Administrator'
    ORGADMIN = 'OrgAdmin'
    DOCTOR = 'Doctor'
    PATIENT = 'Patient'


STATUS_CODES = {
    100: "100 Continue",
    101: "101 Switching Protocols",
    102: "102 Processing",

    200: "200 OK",
    201: "201 Created",
    202: "202 Accepted",
    203: "203 Non-authoritative Information",
    204: "204 No Content",
    205: "205 Reset Content",
    206: "206 Partial Content",
    207: "207 Multi-Status",
    208: "208 Already Reported",
    226: "226 IM Used",

    300: "300 Multiple Choices",
    301: "301 Moved Permanently",
    302: "302 Found",
    303: "303 See Other",
    304: "304 Not Modified",
    305: "305 Use Proxy",
    307: "307 Temporary Redirect",
    308: "308 Permanent Redirect",

    400: "400 Bad Request",
    401: "401 Unauthorized",
    402: "402 Payment Required",
    403: "403 Forbidden",
    404: "404 Not Found",
    405: "405 Method Not Allowed",
    406: "406 Not Acceptable",
    407: "407 Proxy Authentication Required",
    408: "408 Request Timeout",
    409: "409 Conflict",
    410: "410 Gone",
    411: "411 Length Required",
    412: "412 Precondition Failed",
    413: "413 Payload Too Large",
    414: "414 Request-URI Too Long",
    415: "415 Unsupported Media Type",
    416: "416 Requested Range Not Satisfiable",
    417: "417 Expectation Failed",
    418: "418 I'm a teapot",
    421: "421 Misdirected Request",
    422: "422 Unprocessable Entity",
    423: "423 Locked",
    424: "424 Failed Dependency",
    426: "426 Upgrade Required",
    428: "428 Precondition Required",
    429: "429 Too Many Requests",
    431: "431 Request Header Fields Too Large",
    444: "444 Connection Closed Without Response",
    451: "451 Unavailable For Legal Reasons",
    499: "499 Client Closed Request",

    500: "500 Internal Server Error",
    501: "501 Not Implemented",
    502: "502 Bad Gateway",
    503: "503 Service Unavailable",
    504: "504 Gateway Timeout",
    505: "505 HTTP Version Not Supported",
    506: "506 Variant Also Negotiates",
    507: "507 Insufficient Storage",
    508: "508 Loop Detected",
    510: "510 Not Extended",
    511: "511 Network Authentication Required",
    599: "599 Network Connect Timeout Error",
}


class OTPTypes:
    FORGOT = 'forgot'
    LOGIN = 'login'
    VERIFY_USER = 'verify'


OPD_MIN_TIME_IN_SEC = 3600  # 1 HR
OPD_MAX_TIME_IN_SEC = 28800  # 8 HR

distance_of_two_points = 10


class AppointStatus:
    PRE_CONFIRM = 'pre_confirm'
    CONFIRM = 'confirm'
    REQUESTED = 'requested'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
