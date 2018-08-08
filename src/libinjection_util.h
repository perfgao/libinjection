#ifndef __LIBINJECTION_UTIL_H_
#define __LIBINJECTION_UTIL_H_

#include "libinjection_js_data.h"

#include <stddef.h>
#include <stdlib.h>

#define CHAR_NULL '\0'

char bsearch_keywords(const char *src, size_t len,
        keywords_t *words, size_t numb);

#endif
