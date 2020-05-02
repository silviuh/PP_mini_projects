package com.pp.laborator

import khttp.get
import khttp.post
import khttp.responses.Response

@ExperimentalStdlibApi
fun main(args: Array<String>) {

    var kidsBrowser = KidsBrowser(
        CleanGetRequest(GetBrowserRequest("", null, 10000.1)),
        PostBrowserRequest("", null)
    )

    kidsBrowser.start()
}

