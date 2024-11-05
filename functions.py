function_definitions = {
    "functions": [
        {
            "type": "function",
            "function": {
                "name": "make_call",
                "description": "Place a phone call",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact": {
                            "type": "string",
                            "description": "Contact name or phone number",
                        }
                    },
                    "required": ["contact"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "send_message",
                "description": "Send a text message",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient": {"type": "string", "description": "Contact or number"},
                        "message": {"type": "string"},
                    },
                    "required": ["recipient", "message"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "set_alarm",
                "description": "Set an alarm or timer",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "format": "HH:MM",
                            "description": "Time to set alarm for in 24-hour format",
                        },
                        "label": {
                            "type": "string",
                            "description": "Optional label for the alarm",
                        },
                    },
                    "required": ["time"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "create_calendar_event",
                "description": "Create or view calendar events",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "Title of the calendar event",
                        },
                        "start_time": {
                            "type": "string",
                            "format": "date-time",
                            "description": "Start time of the event",
                        },
                        "end_time": {
                            "type": "string",
                            "format": "date-time",
                            "description": "Optional end time of the event",
                        },
                    },
                    "required": ["title", "start_time"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "navigate_to",
                "description": "Get navigation directions to a destination",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination": {
                            "type": "string",
                            "description": "Address or place name to navigate to",
                        },
                        "mode": {
                            "type": "string",
                            "enum": ["driving", "walking", "transit", "cycling"],
                            "description": "Mode of transportation",
                        },
                    },
                    "required": ["destination"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "play_media",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "media_type": {"type": "string", "enum": ["music", "podcast"]},
                        "title": {"type": "string"},
                    },
                    "required": ["media_type", "title"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "control_smart_home",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device": {"type": "string"},
                        "action": {"type": "string", "enum": ["set", "get"]},
                        "value": {"type": "string"},
                    },
                    "required": ["device", "action"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "capture_media",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "type": {"type": "string", "enum": ["photo", "video"]},
                        "camera": {"type": "string", "enum": ["front", "back"]},
                    },
                    "required": ["type"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "set_reminder",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string"},
                        "time": {"type": "string", "format": "date-time"},
                    },
                    "required": ["text", "time"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {"type": "string"},
                        "timeframe": {
                            "type": "string",
                            "enum": ["current", "today", "week"],
                        },
                    },
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "web_search",
                "parameters": {
                    "type": "object",
                    "properties": {"query": {"type": "string"}},
                    "required": ["query"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "read_notifications",
                "parameters": {
                    "type": "object",
                    "properties": {"app": {"type": "string"}, "count": {"type": "integer"}},
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "calculate",
                "description": "Perform mathematical calculations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": "Mathematical expression to evaluate",
                        }
                    },
                    "required": ["expression"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "take_note",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "content": {"type": "string"},
                        "title": {"type": "string"},
                    },
                    "required": ["content"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "control_device_setting",
                "description": "Control device settings like brightness, volume, etc.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "setting": {
                            "type": "string",
                            "enum": [
                                "brightness",
                                "volume",
                                "wifi",
                                "bluetooth",
                                "do_not_disturb",
                                "find_device",
                                "night_mode",
                                "backup",
                            ],
                            "description": "Device setting to control",
                        },
                        "value": {
                            "type": "string",
                            "description": "Value to set (e.g. 'on', 'off', percentage)",
                        },
                    },
                    "required": ["setting", "value"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "send_email",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "to": {"type": "string"},
                        "subject": {"type": "string"},
                        "body": {"type": "string"},
                    },
                    "required": ["to", "subject", "body"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "check_device_status",
                "description": "Check status of device metrics",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "metric": {
                            "type": "string",
                            "enum": ["battery", "storage", "memory"],
                            "description": "Device metric to check",
                        }
                    },
                    "required": ["metric"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "screen_call",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "caller": {"type": "string"},
                        "action": {
                            "type": "string",
                            "enum": ["accept", "reject", "voicemail"],
                        },
                    },
                    "required": ["action"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "track_health",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "metric": {
                            "type": "string",
                            "enum": ["steps", "heart_rate", "sleep", "exercise"],
                        },
                        "timeframe": {"type": "string", "enum": ["today", "week", "month"]},
                    },
                    "required": ["metric"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "launch_app",
                "parameters": {
                    "type": "object",
                    "properties": {"app_name": {"type": "string"}},
                    "required": ["app_name"],
                },
            },
        },
    ]
}
