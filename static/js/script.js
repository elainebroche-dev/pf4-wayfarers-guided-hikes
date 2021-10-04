/* jshint esversion: 8 */
/* globals $, module : false */

// fade out alerts after 5 seconds
document.addEventListener("DOMContentLoaded", fadeAlerts);
    
function fadeAlerts() {
    window.setTimeout(function () {
         $(".alert").fadeTo(1000, 0).slideUp(1000, function () {
            $(this).remove();
         });
    }, 5000);
}

module.exports = fadeAlerts;