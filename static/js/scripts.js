(function($) {
        jQuery(function($){
           $("#date").mask("99/99/9999",{placeholder:"mm/dd/yyyy"});
           $("#id_cpf").mask("(999) 999-9999");
           $("#tin").mask("99-9999999");
           $("#ssn").mask("999-99-9999");
        });
})(grp.jQuery);