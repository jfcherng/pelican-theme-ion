/**
 * open all external links in a new window
 */
$(function() {
  $('a')
    .filter('[href^="http"], [href^="//"]')
    .not('[href*="' + window.location.host + '"]')
    .attr('rel', 'noopener noreferrer')
    .attr('target', '_blank');
});

/**
 * boostrap popover/tooltip
 */
$.fn.popover.Constructor.DEFAULTS.container = 'body';
$.fn.tooltip.Constructor.DEFAULTS.container = 'body';
$(function() {
  $('[data-toggle="popover"]').popover();
  $('[data-toggle="tooltip"]').tooltip();
});

/**
 * remove the trailing asterisk in the table of contents
 */
$(function() {
  $('.toc-href').each(function(idx, el) {
    var asterisk = '\\*';
    var regex = new RegExp(asterisk + '$');

    var $el = $(el);
    var title = $el.text();

    if (regex.test(title)) {
      title = title.replace(regex, '');
      $el.text(title).attr('title', title);
    }
  });
});
