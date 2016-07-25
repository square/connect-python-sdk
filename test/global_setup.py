import json

host_name = 'https://connect.squareupstaging.com'

accounts = json.loads("""{
	"accounts": 
	[{
		"country": "US",
		"email": "dev-platform-acceptance-user+staging@squareup.com",
		"nonsandbox": {
			"isSandbox": "false",
			"accessToken": "x9OMXBALOJxGR0l-90hyrA",
			"locationId": "1DAWGGBYE0J4P",
			"applicationId" : "xQ5V2-aNDh0FwQce_CP2mw",
			"currency": "USD"
		},
		"sandbox": {
			"isSandbox": "true",
			"accessToken": "t6ZDX9L_NVmxC9bw8bBvbg",
			"locationId": "CAISEJHOBBJlXJ4PY9QnoNat_pg",
			"applicationId" : "sandbox-xQ5V2-aNDh0FwQce_CP2mw",
			"currency": "USD"
		}
	},
	{
		"country": "CA",
		"email": "dev-platform-acceptance-userstaging-eh@squareup.com",
		"nonsandbox": {
			"isSandbox": "false",
			"accessToken": "sq0ats-jzmryigm2B6baiqP94geZQ",
			"locationId": "BTJNR7800H43V",
			"applicationId" : "sq0ids-wwfhxQuGYmRHjjKRsl64iA",
			"currency": "CAD"
		},
		"sandbox": {
			"isSandbox": "true",
			"accessToken": "sq0atb-25A4V_ztOeT6TTJ2VJWgEQ",
			"locationId": "CAISEJHOBBJlXJ4PY9QnoNat_pg",
			"applicationId" : "sandbox-sq0ids-wwfhxQuGYmRHjjKRsl64iA",
			"currency": "CAD"
		}
	},
	{
		"country": "US",
		"email": "tpan+test@squareup.com",
		"nonsandbox": {
			"isSandbox": "false",
			"accessToken": "sq0atp-zzDoZHEoaXFOUW-jw3TbuQ",
			"locationId": "351RYX7Y7NBGY",
			"applicationId" : "sq0idp-Kb8uC00772WG0jpU5Q5ScQ",
			"currency": "USD"
		},
		"sandbox": {
			"isSandbox": "true",
			"accessToken": "sq0atb-44gzjrtZTseuJK5BQqCfbg",
			"locationId": "CBASEFU1QAw5oZ261gN6WWyCXfA",
			"applicationId" : "sandbox-sq0idp-Kb8uC00772WG0jpU5Q5ScQ",
			"currency": "USD"
		}
	}]
	}""")

account = accounts['accounts'][0]["nonsandbox"]


