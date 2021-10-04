/**
 * @jest-environment jsdom
 */
/* jshint esversion: 8 */
/* globals $, global, require, jest, beforeEach, afterEach : false */
/* globals describe, test, expect  : false */

global.window = window;
global.$ = require('jquery');

const fadeAlerts = require("../script");

jest.setTimeout(10000);  

beforeEach(() => {
    $.fx.off = true; // Disable jQuery animations
    document.body.innerHTML = "<div><div class='alert alert-success' role='alert'>middle bit</div></div>";
});

afterEach(() => {
    $.fx.off = false; // Enable jQuery animations
});

describe("DOM alert class test", () => {
    test('check alert element is removed', async () => {
        let before = document.getElementsByClassName("alert").length;
        expect(before == 1).toBeTruthy();
        fadeAlerts();  // test jquery code removes the element with alert class
        await new Promise((r) => setTimeout(r, 7000));
        let after = document.getElementsByClassName("alert").length;
        expect(after == 0).toBeTruthy();
      });
 });
