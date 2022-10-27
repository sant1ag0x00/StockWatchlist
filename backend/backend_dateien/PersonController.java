package com.stocks.stockwatchlist;

import org.springframework.web.bind.annotation.RestController;

@RestController
public class PersonController{

    @GetMapping("/person")
    public Person response() {
        return null;
    }
}