package com.pp.laborator

open class GenericBrowserRequest(url: String, map: Map<String, String>?) : Cloneable {

    var url: String = ""
    var params: Map<String, String>? = null

    init {
        this.url = url
        this.params = map
    }

    override fun clone(): Any {
        return super.clone()
    }
}