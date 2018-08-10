#!/usr/bin/env python

"""
form https://developer.mozilla.org/zh-CN/docs/Web/Events
"""

import sys

def parse(obj):
    print ("""#ifndef __LIBINJECTION_JS_DATA_H__
#define __LIBINJECTION_JS_DATA_H__

#include <stddef.h>

typedef struct {
    const char* word;
    const char  type;
} keywords_t;

""")

    eventwords = obj["events"]
    flag = 'f'

    lowerEvents = set([x.lower() for x in eventwords])

    print ("static const keywords_t js_keywords[] = {")

    for k in sorted(lowerEvents):
        print ("    {\"%s\", '%s'}," % (k, flag))

    print ("};\n")
    print ("static const size_t js_keywords_len = %d;\n" % (len(eventwords)))

    print ("#endif")



if __name__ == '__main__':
    import json
    sys.exit(parse(json.load(sys.stdin)))
