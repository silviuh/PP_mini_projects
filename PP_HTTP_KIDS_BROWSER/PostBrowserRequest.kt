package com.pp.laborator

import khttp.responses.Response

class PostBrowserRequest(url: String, params: Map<String, String>?) {

    var genericRequest: GenericBrowserRequest? = null

    init {
        genericRequest = GenericBrowserRequest(url, params)
    }

    fun setParams(URL: String, map: Map<String, String>) {
        this.genericRequest!!.url = URL
        this.genericRequest!!.params = map
    }

    fun postRequest(): Response {
        return khttp.post(this.genericRequest!!.url, data=genericRequest!!.params)
    }
}