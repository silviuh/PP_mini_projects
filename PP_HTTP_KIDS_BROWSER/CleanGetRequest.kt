package com.pp.laborator

import khttp.responses.Response

class CleanGetRequest(getReq: GetBrowserRequest) : HTTPGet {

    final var NR_OF_FORBIDDEN_LINKS = 1000
    final var NR_OF_FORBIDDEN_WORDS = 1000
    var parentalControlDisallow: List<String>? = null
    var forbiddenAccessLinks: ArrayList<String>? = arrayListOf()
    var forbiddenWordsList: ArrayList<String>? = arrayListOf()

    var getRequest: GetBrowserRequest? = null

    init {
        this.getRequest = getReq
        this.forbiddenAccessLinks!!.add("https://www.pornhub.com/")
        this.forbiddenAccessLinks!!.add("https://www.tblop.com/load/chaturbate/")
        this.forbiddenAccessLinks!!.add("https://xhamster.com/")
        this.forbiddenAccessLinks!!.add("https://www.xvideos.com/")
        this.forbiddenAccessLinks!!.add("https://www.redtube.com/")
        this.forbiddenAccessLinks!!.add("https://www.xnxx.com/")
        this.forbiddenAccessLinks!!.add("https://www.pornhub.com/")
        this.forbiddenAccessLinks!!.add("https://www.tube8.com/")
        this.forbiddenAccessLinks!!.add("https://www.buttnakednasty.com/")
        this.forbiddenAccessLinks!!.add("http://pornerbros.com/?wmid=561&sid=1")
        this.forbiddenAccessLinks!!.add("http://www.hdporn.net/")
        this.forbiddenAccessLinks!!.add("http://www.spankbang.com/")
        this.forbiddenAccessLinks!!.add("https://www.youporn.com/")
        this.forbiddenAccessLinks!!.add("https://smutr.com/")

        this.forbiddenWordsList!!.add("([Pp][Oo][Rr][Nn])")
        this.forbiddenWordsList!!.add("([Ss][Ee][Xx])")
        this.forbiddenWordsList!!.add("lesbian")
        this.forbiddenWordsList!!.add("gay")
        this.forbiddenWordsList!!.add("fuck")
        this.forbiddenWordsList!!.add("hot")
        this.forbiddenWordsList!!.add("sexy")
        this.forbiddenWordsList!!.add("masturbate")
        this.forbiddenWordsList!!.add("fetish")
    }


    fun setURL(URL: String) {
        getRequest!!.setURL(URL)
    }

    override fun getResponse(): Response? {
        var i = 0
        for (i in 0 until this.forbiddenAccessLinks!!.size) {
            if (this.forbiddenAccessLinks!![i]
                == this.getRequest!!
                    .getURL()
            ) {
                return null
            }
        }

        i = 0
        for (i in 0 until this.forbiddenWordsList!!.size) {
            if (this.forbiddenWordsList!![i]
                    .toRegex()
                    .containsMatchIn(
                        this.getRequest!!
                            .getURL()
                    )
            ) {
                return null
            }
        }

        return getRequest!!.getResponse() // proxy test passed
    }
}