package com.pp.laborator

import khttp.post
import sun.security.pkcs11.wrapper.CK_AES_CTR_PARAMS
import javax.swing.text.html.HTML
import javax.swing.text.html.HTMLDocument

class KidsBrowser(cleanReq: CleanGetRequest, postReq: PostBrowserRequest?) {

    var cleanRequest: CleanGetRequest? = null
    var postRequest: PostBrowserRequest? = null
    var sesionIsOn: Boolean = true
    var URL: String = ""

    init {
        this.cleanRequest = cleanReq
        this.postRequest = postReq
    }

    @ExperimentalStdlibApi
    fun start() {
        while (sesionIsOn) {
            print("\n\n\n\n\n\n")
            println("----------------------------------------------------------------------------")
            println("WELCOME TO KIDS BROWSER SESSION...[ V.01 ]")
            println("                                   MENU")
            println("                  1. Get HTTP request + print response body")
            println("                  2. POST HTTP request")
            println("                  3. Exit")
            println("----------------------------------------------------------------------------")

            println("\nYour input: ")
            var input = readLine()!!.toInt()

            when (input) {
                1 -> {
                    println("URL: ")
                    this.URL = readLine()!!.toString()
                    Thread.sleep(2000)

                    cleanRequest!!.setURL(this.URL)
                    var response = cleanRequest!!.getResponse()

                    if (response == null) {
                        println("!!! [ YOU TRIED TO ACCESS A FORBIDDEN WEBSITE! ] !!!")
                    } else {
                       var byteStream = response.content.decodeToString()
                       println(byteStream)

                    }
                }

                2 -> {
                    println("URL: ")
                    this.URL = readLine()!!.toString()
                    Thread.sleep(2000)

                    println("Name: ")
                    var name = readLine()!!.toString()
                    Thread.sleep(1000)

                    println("Password: ")
                    var password = readLine()!!.toString()
                    Thread.sleep(1000)

                    this.postRequest!!.setParams(
                        this.URL, mapOf(name.toString() to password.toString())
                    )

                    var response = this.postRequest!!.postRequest()
                    println(response.text)
                }

                3 -> {
                    println("SESSION ENDED ...")
                    this.sesionIsOn = false
                }

            }

        }
    }
}