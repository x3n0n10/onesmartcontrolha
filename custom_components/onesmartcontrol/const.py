# Actions
ACTION_ADD = "add"
ACTION_CHECK = "check"
ACTION_DELETE = "delete"
ACTION_GET = "get"
ACTION_LIST = "list"
ACTION_PERFORM = "perform"
ACTION_SUBSCRIBE = "subscribe"
ACTION_TOTAL = "total"
ACTION_UPDATE = "update"

CONNECT_SUCCESS = 0
CONNECT_FAIL_NETWORK = 1
CONNECT_FAIL_AUTH = 2

# Commands
COMMAND_APPARATUS = "apparatus"
COMMAND_AUTHENTICATE = "authenticate"
COMMAND_DEVICE = "device"
COMMAND_ENERGY = "energy"
COMMAND_EVENTS = "events"
COMMAND_GETTOKEN = "gettoken"
COMMAND_LOGBOOK = "logbook"
COMMAND_METER = "meter"
COMMAND_MODULES = "modules"
COMMAND_PING = "ping"
COMMAND_PRESET = "preset"
COMMAND_PRESET_GROUP = "presetgroup"
COMMAND_ROLE = "role"
COMMAND_ROOM = "room"
COMMAND_SITE = "site"
COMMAND_USER = "user"
COMMAND_UPGRADE = "upgrade"
COMMAND_SITEPRESET = "sitepreset"
COMMAND_TRIGGER = "trigger"

DEVICE_MANUFACTURER = "One Smart Control"
INTEGRATION_TITLE = "One Smart Control"

DOMAIN = "onesmartcontrol"
ONESMART_RUNNER = "runner"
ONESMART_WRAPPER = "onesmartwrapper"
ONESMART_UPDATE_PUSH = f"{DOMAIN}_push"
ONESMART_UPDATE_POLL = f"{DOMAIN}_poll"
ONESMART_UPDATE_DEFINITIONS = f"{DOMAIN}_definitions"

EVENT_ENERGY_CONSUMPTION = "energy_consumption"

SCAN_INTERVAL_DEFINITIONS = 1800
SCAN_INTERVAL_CACHE = 60

INTERVAL_TRACKER_DEFINITIONS = "track_interval_definitions"
INTERVAL_TRACKER_POLL = "track_interval_poll"

RPC_ACTION = "action"
RPC_COMMAND = "cmd"
RPC_DATA = "data"
RPC_ERROR = "error"
RPC_EVENT = "event"
RPC_RESULT = "result"
RPC_TRANSACTION = "transaction"
RPC_VALUES = "values"
RPC_VALUE = "value"
RPC_NAME = "name"
RPC_METERS = "meters"
RPC_ID = "id"


SITE_NODEID = "nodeID"
SITE_MAC = "mac"
SITE_VERSION = "version"

TOPIC_AUTHENTICATION = "AUTHENTICATION"
TOPIC_ENERGY = "ENERGY"
TOPIC_DEVICE = "DEVICE",
TOPIC_MESSAGE = "MESSAGE"
TOPIC_METER = "METER"
TOPIC_PRESET = "PRESET"
TOPIC_PRESETGROUP = "PRESETGROUP"
TOPIC_ROLE = "ROLE"
TOPIC_ROOM = "ROOM"
TOPIC_TRIGGER = "TRIGGER"
TOPIC_SITE = "SITE"
TOPIC_SITEPRESET = "SITEPRESET"
TOPIC_UPGRADE = "UPGRADE"
TOPIC_USER = "USER"


ALL_TOPICS = [
    TOPIC_AUTHENTICATION, TOPIC_DEVICE, TOPIC_ENERGY, 
    TOPIC_MESSAGE, TOPIC_METER, TOPIC_PRESET, 
    TOPIC_PRESETGROUP, TOPIC_ROLE, TOPIC_ROOM, 
    TOPIC_TRIGGER, TOPIC_SITE, TOPIC_SITEPRESET,
    TOPIC_UPGRADE, TOPIC_USER
]

# Config
SOCKET_BUFFER_SIZE = 1024
SOCKET_RECEIVE_TIMEOUT = 1
MAX_TRANSACTION_ID = 65535
PING_INTERVAL = 30
DEFAULT_PORT = 9010
