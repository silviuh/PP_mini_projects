package com.pp.laborator

import khttp.responses.Response

class GetBrowserRequest(url: String, params: Map<String, String>?, timeout: Double) : HTTPGet {

    var timeout: Double = 0.0
    var genericRequest: GenericBrowserRequest? = null

    init {
        genericRequest = GenericBrowserRequest(url, params)
        this.timeout = timeout
    }

    fun setURL(URL: String) {
        genericRequest!!.url = URL
    }

    fun getURL(): String {
        return genericRequest!!.url
    }

    override fun getResponse(): Response {
        return khttp.get(this.genericRequest!!.url, timeout = this.timeout)
    }
}