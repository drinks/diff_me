/**
 * Diff.me js
 * @author Dan Drinkard <dan.drinkard@gmail.com>
 * @requires jQuery
 */
(function($){
    $(function(){
        difftable = $('table.diff');
        difftable.find('td.diff_text').each(function(){
            $(this).html($(this).html().replace('  ', '&nbsp;&nbsp;'));
        });
        difftable.find('tr:nth-child(even)').addClass('even')
        difftable.find('tr:nth-child(odd)').addClass('odd')
        // difftable.find('colgroup').remove();
        // difftable.prepend('<colgroup class="original"><col class="shortcuts" /><col class="linenos" /><col class="text" /></colgroup><colgroup class="modified"><col class="shortcuts" /><col class="linenos" /><col class="text" /></colgroup>');
        $('.diff_sub').each(function(){
            if($(this).siblings().filter('.diff_add, .diff_chg').length == 0){
                $(this).parent('td').addClass('ctx_sub');
            }else{
                $(this).parent('td').addClass('ctx_diff');
            }
        });
        $('.diff_add').each(function(){
            if($(this).siblings().filter('.diff_sub, .diff_chg').length == 0){
                $(this).parent('td').addClass('ctx_add');
            }else{
                $(this).parent('td').addClass('ctx_diff');
            }
        });
    });
})(jQuery);