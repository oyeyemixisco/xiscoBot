
$(document).ready(function($) {
	
	// Variables declarations
	var $wrapper = $('.main-wrapper');
	var $pageWrapper = $('.page-wrapper');
	var $slimScrolls = $('.slimscroll');
	var $sidebarOverlay = $('.sidebar-overlay');
	
	// Sidebar
	var Sidemenu = function() {
		this.$menuItem = $('#sidebar-menu a');
	};

	function init() {
		var $this = Sidemenu;
		$('#sidebar-menu a').on('click', function(e) {
			if($(this).parent().hasClass('submenu')) {
				e.preventDefault();
			}
			if(!$(this).hasClass('subdrop')) {
				$('ul', $(this).parents('ul:first')).slideUp(350);
				$('a', $(this).parents('ul:first')).removeClass('subdrop');
				$(this).next('ul').slideDown(350);
				$(this).addClass('subdrop');
			} else if($(this).hasClass('subdrop')) {
				$(this).removeClass('subdrop');
				$(this).next('ul').slideUp(350);
			}
		});
		$('#sidebar-menu ul li.submenu a.active').parents('li:last').children('a:first').addClass('active').trigger('click');
	}
	// Sidebar Initiate
	init();
	
	// Sidebar overlay
	function sidebar_overlay($target) {
		if($target.length) {
			$target.toggleClass('opened');
			$sidebarOverlay.toggleClass('opened');
			$('html').toggleClass('menu-opened');
			$sidebarOverlay.attr('data-reff', '#' + $target[0].id);
		}
	}
	
	// Mobile menu sidebar overlay
	$(document).on('click', '#mobile_btn', function() {
		var $target = $($(this).attr('href'));
		sidebar_overlay($target);
		$wrapper.toggleClass('slide-nav');
		$('#chat_sidebar').removeClass('opened');
		return false;
	});
	
	// Chat sidebar overlay
	$(document).on('click', '#task_chat', function() {
		var $target = $($(this).attr('href'));
		console.log($target);
		sidebar_overlay($target);
		return false;
	});
	
	// Sidebar overlay reset
	$sidebarOverlay.on('click', function() {
		var $target = $($(this).attr('data-reff'));
		if($target.length) {
			$target.removeClass('opened');
			$('html').removeClass('menu-opened');
			$(this).removeClass('opened');
			$wrapper.removeClass('slide-nav');
		}
		return false;
	});
	
	// Password
	if($('.toggle-password').length > 0) {
		$(document).on('click', '.toggle-password', function() {
			$(this).toggleClass("feather-eye-off feather-eye");
			var input = $(".pass-input");
			if (input.attr("type") == "password") {
				input.attr("type", "text");
			} else {
				input.attr("type", "password");
			}
		});
	}
	if($('.confirm-password').length > 0) {
		$(document).on('click', '.confirm-password', function() {
			$(this).toggleClass("feather-eye-off feather-eye");
			var input = $(".pass-input-confirm");
			if (input.attr("type") == "password") {
				input.attr("type", "text");
			} else {
				input.attr("type", "password");
			}
		});
	}
	
	// Circle Progress Bar
	function animateElements() {
		$('.circle-bar2').each(function () {
			var elementPos = $(this).offset().top;
			var topOfWindow = $(window).scrollTop();
			var percent = $(this).find('.circle-graph2').attr('data-percent');
			var animate = $(this).data('animate');
			if (elementPos < topOfWindow + $(window).height() - 30 && !animate) {
				$(this).data('animate', true);
				$(this).find('.circle-graph2').circleProgress({
					value: percent / 100,
					size : 400,
					thickness: 30,
					fill: {
						color: '#2E37A4'
					}
				});
			}
		});
	}	
	
	if($('.circle-bar').length > 0) {
		animateElements();
	}
	$(window).scroll(animateElements);
	
	// Select 2
	if($('.select').length > 0) {
		$('.select').select2({
			minimumResultsForSearch: -1,
			width: '100%'
		});
	}
	
	// Floating Label
	if($('.floating').length > 0) {
		$('.floating').on('focus blur', function(e) {
			$(this).parents('.form-focus').toggleClass('focused', (e.type === 'focus' || this.value.length > 0));
		}).trigger('blur');
	}
	
	// Right Sidebar Scroll
	if($('#msg_list').length > 0) {
		$('#msg_list').slimscroll({
			height: '100%',
			color: '#878787',
			disableFadeOut: true,
			borderRadius: 0,
			size: '4px',
			alwaysVisible: false,
			touchScrollStep: 100
		});
		var msgHeight = $(window).height() - 124;
		$('#msg_list').height(msgHeight);
		$('.msg-sidebar .slimScrollDiv').height(msgHeight);
		$(window).resize(function() {
			var msgrHeight = $(window).height() - 124;
			$('#msg_list').height(msgrHeight);
			$('.msg-sidebar .slimScrollDiv').height(msgrHeight);
		});
	}
	
	// Left Sidebar Scroll
	if($slimScrolls.length > 0) {
		$slimScrolls.slimScroll({
			height: 'auto',
			width: '100%',
			position: 'right',
			size: '7px',
			color: '#ccc',
			wheelStep: 10,
			touchScrollStep: 100
		});
		var wHeight = $(window).height() - 60;
		$slimScrolls.height(wHeight);
		$('.sidebar .slimScrollDiv').height(wHeight);
		$(window).resize(function() {
			var rHeight = $(window).height() - 60;
			$slimScrolls.height(rHeight);
			$('.sidebar .slimScrollDiv').height(rHeight);
		});
	}
	
	// Page wrapper height
	var pHeight = $(window).height();
	$pageWrapper.css('min-height', pHeight);
	$(window).resize(function() {
		var prHeight = $(window).height();
		$pageWrapper.css('min-height', prHeight);
	});
	

	if($('.summernote').length > 0) {
		//var editorheight = $('.editor-card').height()-100;
        $('.summernote').summernote({
			placeholder: 'Description',
		    focus: true,
			minHeight: 100,
			disableResizeEditor: false,
			toolbar: [
				['fullscreen',],
				['fontname', ['fontname']],
				['undo'],
				['redo'],
				['datetimepicker'],
				['fontsize', ['fontsize']],
				['font', ['bold', 'italic', 'underline', 'clear']],
				['color', ['color']],
				['para', ['ul', 'ol', 'paragraph']],
				['insert', ['link', 'picture']]
			  ],
			// set focus to editable area after initializing summernote
		});
    }

	// Summernote
	
	if($('#summernote').length > 0) {
        $('#summernote').summernote({
		  height: 300,                 // set editor height
		  minHeight: null,             // set minimum height of editor
		  maxHeight: null,             // set maximum height of editor
		  focus: true                  // set focus to editable area after initializing summernote
		});
    }
	// editor
	if ($('#editor').length > 0) {
		ClassicEditor
		.create( document.querySelector( '#editor' ), {
			toolbar: {
                items: [
                    'heading', '|',
                    'fontfamily', 'fontsize', '|',
                    'alignment', '|', 
                    'fontColor', 'fontBackgroundColor', '|',
                    'bold', 'italic', 'strikethrough', 'underline', 'subscript', 'superscript', '|',
                    'link', '|',
                    'outdent', 'indent', '|',
                    'bulletedList', 'numberedList', 'todoList', '|',
                    'code', 'codeBlock', '|',
                    'insertTable', '|',
                    'uploadImage', 'blockQuote', '|',
                    'undo', 'redo'
                ],
                shouldNotGroupWhenFull: true
            }
		} )
		.then( editor => {
			window.editor = editor;
		} )
		.catch( err => {
			console.error( err.stack );
		} );
	}

	// Counter 
	
	if($('.counter').length > 0) {
		$('.counter').counterUp({
			 delay: 20,
			 time: 2000
		});
	 }
	 
	 if($('#timer-countdown').length > 0) {
		 $( '#timer-countdown' ).countdown( {
			 from: 180, // 3 minutes (3*60)
			 to: 0, // stop at zero
			 movingUnit: 1000, // 1000 for 1 second increment/decrements
			 timerEnd: undefined,
			 outputPattern: '$day Day $hour : $minute : $second',
			 autostart: true
		 });
	 }
	 
	 if($('#timer-countup').length > 0) {
		 $( '#timer-countup' ).countdown( {
			 from: 0,
			 to: 180 
		 });
	 }
	 
	 if($('#timer-countinbetween').length > 0) {
		 $( '#timer-countinbetween' ).countdown( {
			 from: 30,
			 to: 20 
		 });
	 }
	 
	 if($('#timer-countercallback').length > 0) {
		 $( '#timer-countercallback' ).countdown( {
			 from: 10,
			 to: 0,
			 timerEnd: function() {
				 this.css( { 'text-decoration':'line-through' } ).animate( { 'opacity':.5 }, 500 );
			 } 
		 });
	 }
	 
	 if($('#timer-outputpattern').length > 0) {
		 $( '#timer-outputpattern' ).countdown( {
			 outputPattern: '$day Days $hour Hour $minute Min $second Sec..',
			 from: 60 * 60 * 24 * 3
		 });
	 }

	 // Clipboard 
	
	if($('.clipboard').length > 0) {
		var clipboard = new Clipboard('.btn');
	}
	// Popover
	
	if($('.popover-list').length > 0) {
		var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
		var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
		  return new bootstrap.Popover(popoverTriggerEl)
		})
	}

	// Form Wizard
	
	$(".next").on('click', function () { // Function Runs On NEXT Button Click
		$(this).closest('.tab-pane').next().css("display" , "block").css("opacity" , "1");
		$(this).closest('.tab-pane').css({
			'display': 'none'
		});
	
	});
	$(".previous").on('click', function () { // Function Runs On NEXT Button Click
		$(this).closest('.tab-pane').prev().css("display", "block");
		$(this).closest('.tab-pane').css({
			'display': 'none'
		});
	
	});
	// Tooltip

	if($('[data-bs-toggle="tooltip"]').length > 0) {
		$('[data-bs-toggle="tooltip"]').tooltip();
	}

	if($('.custom-file-container').length > 0) {
        //First upload
        var firstUpload = new FileUploadWithPreview('myFirstImage')
        //Second upload
        var secondUpload = new FileUploadWithPreview('mySecondImage')
	}
		
	// CK Editor

	if ($('#editor').length > 0) {
		ClassicEditor
		.create( document.querySelector( '#editor' ), {
			 toolbar: {
			    items: [
			        'heading', '|',
			        'fontfamily', 'fontsize', '|',
			        'alignment', '|',
			        'fontColor', 'fontBackgroundColor', '|',
			        'bold', 'italic', 'strikethrough', 'underline', 'subscript', 'superscript', '|',
			        'link', '|',
			        'outdent', 'indent', '|',
			        'bulletedList', 'numberedList', 'todoList', '|',
			        'code', 'codeBlock', '|',
			        'insertTable', '|',
			        'uploadImage', 'blockQuote', '|',
			        'undo', 'redo'
			    ],
			    shouldNotGroupWhenFull: true
			}
		} )
		.then( editor => {
			window.editor = editor;
		} )
		.catch( err => {
			console.error( err.stack );
		} );
	}
	// Datatable
	if($('.datatable').length > 0) {
		$('.datatable').DataTable({
			"bFilter": false,
			"language": {
			paginate: {
				next: 'Next',
				previous: 'Previous'
			},
		}
		});
	}
	
	// Time
	if($('#datetimepicker3').length > 0) {
		$(function () {
			$('#datetimepicker3').datetimepicker({
				format: 'LT',
				icons: {
					up: "fas fa-angle-up",
					down: "fas fa-angle-down",
					next: 'fas fa-angle-right',
					previous: 'fas fa-angle-left'
				}
			});
		});
	}
	if($('#datetimepicker4').length > 0) {
		$(function () {
			$('#datetimepicker4').datetimepicker({
				format: 'LT',
				icons: {
					up: "fas fa-angle-up",
					down: "fas fa-angle-down",
					next: 'fas fa-angle-right',
					previous: 'fas fa-angle-left'
				}
			});
		});
	}
	
	
	
	// slick
	if($('.center').length > 0) {
		$('.center').slick({
		  centerMode: true,
		  arrows: false,
		  centerPadding: '30px',
		  slidesToShow: 3,
		  responsive: [
			{
			  breakpoint: 768,
			  settings: {
				arrows: false,
				centerMode: true,
				centerPadding: '40px',
				slidesToShow: 3
			  }
			},
			{
			  breakpoint: 480,
			  settings: {
				arrows: false,
				centerMode: true,
				centerPadding: '40px',
				slidesToShow: 3
			  }
			}
		  ]
		});
	}
	
	// Bootstrap Tooltip
	if($('[data-toggle="tooltip"]').length > 0) {
		$('[data-toggle="tooltip"]').tooltip();
	}
	
	// Mobile Menu
	$(document).on('click', '#open_msg_box', function() {
		$wrapper.toggleClass('open-msg-box');
		return false;
	});
	
	// Lightgallery
	if($('#lightgallery').length > 0) {
		$('#lightgallery').lightGallery({
			thumbnail: true,
			selector: 'a'
		});
	}
	
	// Incoming call popup
	if($('#incoming_call').length > 0) {
		$('#incoming_call').modal('show');
	}
	
	// JQuery counterUp

	if($('.dash-count .counter-up').length > 0) {
		$('.dash-count .counter-up').counterUp({
            delay: 15,
            time: 1500
        });
	}
	
	// Summernote
	if($('.summernote').length > 0) {
		$('.summernote').summernote({
			height: 200,
			minHeight: null,
			maxHeight: null,
			focus: false
		});
	}
	
	// Check all email
	$(document).on('click', '#check_all', function() {
		$('.checkmail').click();
		return false;
	});
	if($('.checkmail').length > 0) {
		$('.checkmail').each(function() {
			$(this).on('click', function() {
				if($(this).closest('tr').hasClass('checked')) {
					$(this).closest('tr').removeClass('checked');
				} else {
					$(this).closest('tr').addClass('checked');
				}
			});
		});
	}
	
	// Mail important
		$(document).on('click', '.mail-important', function() {
		$(this).find('i.fa').toggleClass('fa-star').toggleClass('fa-star-o');
	});
	
	// Dropfiles
	if($('#drop-zone').length > 0) {
		var dropZone = document.getElementById('drop-zone');
		var uploadForm = document.getElementById('js-upload-form');
		var startUpload = function(files) {
			console.log(files);
		};
		uploadForm.addEventListener('submit', function(e) {
			var uploadFiles = document.getElementById('js-upload-files').files;
			e.preventDefault();
			startUpload(uploadFiles);
		});
		dropZone.ondrop = function(e) {
			e.preventDefault();
			this.className = 'upload-drop-zone';
			startUpload(e.dataTransfer.files);
		};
		dropZone.ondragover = function() {
			this.className = 'upload-drop-zone drop';
			return false;
		};
		dropZone.ondragleave = function() {
			this.className = 'upload-drop-zone';
			return false;
		};
	}
	
	// Small Sidebar
	if(screen.width >= 992) {
		$(document).on('click', '#toggle_btn', function() {
			if($('body').hasClass('mini-sidebar')) {
				$('body').removeClass('mini-sidebar');
				$('.subdrop + ul').slideDown();
			} else {
				$('body').addClass('mini-sidebar');
				$('.subdrop + ul').slideUp();
			}
			return false;
		});
		$(document).on('mouseover', function(e) {
			e.stopPropagation();
			if($('body').hasClass('mini-sidebar') && $('#toggle_btn').is(':visible')) {
				var targ = $(e.target).closest('.sidebar').length;
				if(targ) {
					$('body').addClass('expand-menu');
					$('.subdrop + ul').slideDown();
				} else {
					$('body').removeClass('expand-menu');
					$('.subdrop + ul').slideUp();
				}
				return false;
			}
		});
	}
	if ($('[data-feather]').length > 0) {
		feather.replace();
		}
	// Checkbox Select
	
		$('.app-listing .selectBox').on("click", function() {
			$(this).parent().find('#checkBoxes').fadeToggle();
			$(this).parent().parent().siblings().find('#checkBoxes').fadeOut();
		});

		$('.invoices-main-form .selectBox').on("click", function() {
			$(this).parent().find('#checkBoxes-one').fadeToggle();
			$(this).parent().parent().siblings().find('#checkBoxes-one').fadeOut();
		});
	// Invoices Checkbox Show

		$(function() {
			$("input[name='invoice']").click(function() {
				if ($("#chkYes").is(":checked")) {
					$("#show-invoices").show();
				} else {
					$("#show-invoices").hide();
				}
			});
		});
		// Invoices Table Add More
	
		$(".add-table-items").on('click','.remove-btn', function () {
			$(this).closest('.add-row').remove();
			return false;
		});
		 // Editor
		if ($('#editor').length > 0) {
			ClassicEditor
			.create( document.querySelector( '#editor' ), {
				toolbar: [  'bold', 'italic', 'link' ]
			} )
			.then( editor => {
				window.editor = editor;
			} )
			.catch( err => {
				console.error( err.stack );
			} );
		}
		$(document).on("click",".add-links1",function () {
			var experiencecontent = '<div class="links-cont">' +
				'<div class="service-amount">' +
					'<a href="#" class="service-trash1"><i class="fa fa-minus-circle me-1"></i>Service Charge</a> <span>$ 4</span' +
				'</div>' +
			'</div>';
			
			$(".links-info-one").append(experiencecontent);
			return false;
		});
		$(".links-info-one").on('click','.service-trash1', function () {
			$(this).closest('.links-cont').remove();
			return false;
		});
		
		
		 $(".links-info-discount").on('click','.service-trash-one', function () {
			$(this).closest('.links-cont-discount').remove();
			return false;
		});
		// Logo Hide Btn

		$(document).on("click",".logo-hide-btn",function () {
			$(this).parent().hide();
		});
		
		$(document).on("click",".add-btns",function () {
			var experiencecontent = '<tr class="add-row">' +
				'<td>' +
					'<input type="text" class="form-control">' +
				'</td>' +
				'<td>' +
					'<input type="text" class="form-control">' +
				'</td>' +
				'<td>' +
					'<input type="text" class="form-control">' +
				'</td>' +
				'<td>' +
					'<input type="text" class="form-control">' +
				'</td>' +
				'<td>' +
					'<input type="text" class="form-control">' +
				'</td>' +
				'<td>' +
					'<input type="text" class="form-control">' +
				'</td>' +
				'<td class="add-remove text-end">' +
				' <a href="javascript:void(0);" class="add-btns me-2"><i class="fas fa-plus-circle"></i></a> ' +
				' <a href="#" class="copy-btn me-2"><i class="fas fa-copy"></i></a>' +
				'<a href="javascript:void(0);" class="remove-btn"><i class="fa fa-trash-alt"></i></a>' +
				'</td>' +
			'</tr>';
			
			$(".add-table-items").append(experiencecontent);
			return false;
		});
		$(document).on("click",".add-links",function () {
			var experiencecontent = '<div class="links-info"><div class="row form-row links-cont">' +
					'<div class="input-block form-placeholder d-flex">' +
						'<button class="btn social-icon"><i class="feather-github"></i></button>' +
						'<input type="text" class="form-control" placeholder="Social Link">' +
						'<a href="#" class="btn trash">' +
						'<i class="feather-trash-2"></i>' +
						'</a>'+
					'</div>' +
				'</div>' +
			'</div>';
			
			$(".settings-form").append(experiencecontent);
			return false;
		});
		$(".settings-form").on('click','.trash', function () {
			$(this).closest('.links-cont').remove();
			return false;
		});
});





document.addEventListener('DOMContentLoaded', () => {
  const video = document.getElementById('loginVideo');
  const muteBtn = document.getElementById('muteBtn');

  // ✅ If not on the login page, don't run this code
  if (!video || !muteBtn) return;

  function syncMuteUI() {
    muteBtn.classList.toggle('muted', video.muted);
    muteBtn.setAttribute('aria-label', video.muted ? 'Unmute video' : 'Mute video');
  }

  syncMuteUI();

  muteBtn.addEventListener('click', () => {
    video.muted = !video.muted;
    syncMuteUI();
  });

  video.addEventListener('volumechange', syncMuteUI);
});



document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('darkModeToggle');
    const body = document.body;

    // 1. Check for saved preference
    if (localStorage.getItem('theme') === 'dark') {
        body.classList.add('dark-theme');
    }

    // 2. Add click event
    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            body.classList.toggle('dark-theme');
            
            // 3. Save preference
            if (body.classList.contains('dark-theme')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });
    }
});

let lastAiResponse = "";

const textarea = document.getElementById('chatInput');
const sendBtn = document.getElementById('sendBtn');

const welcomeSection = document.getElementById('welcomeSection');
const chatMessages = document.getElementById('chatMessages');
const inputWrapper = document.getElementById('inputWrapper');
const messageList = document.getElementById('messageList');
const chatInput = document.getElementById('chatInput');


textarea.addEventListener('input', function() {
    // 1. Auto-expand height
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';

    // 2. Toggle button color based on content
    if (this.value.trim().length > 0) {
        sendBtn.classList.add('active');
    } else {
        sendBtn.classList.remove('active');
    }
});

let activeTTS = { btn: null, speaking: false };


async function sendMessage() {
	document.dispatchEvent(new Event("mousemove"));
  const text = chatInput.value.trim();
  if (!text) return;

  // UI Transition
  if (welcomeSection && window.getComputedStyle(welcomeSection).display !== 'none') {
    welcomeSection.style.display = 'none';
    chatMessages.style.display = 'block';
    inputWrapper.classList.remove('initial-state');
    inputWrapper.classList.add('chatting-mode');
    document.body.classList.add('chatting-mode-active');
  }

  // User message (SAFE)
  const userWrapper = document.createElement('div');
  userWrapper.className = 'chat-message-wrapper user-side';

  const avatar = document.createElement('div');
  avatar.className = 'avatar';
  avatar.innerHTML = `<img src="/static/img/user1.jpg">`;

  const msg = document.createElement('div');
  msg.className = 'message user-msg';
  msg.textContent = text;

  userWrapper.appendChild(avatar);
  userWrapper.appendChild(msg);
  messageList.appendChild(userWrapper);

  chatInput.value = "";
  chatInput.style.height = 'auto';
  sendBtn.classList.remove('active');

  // AI typing bubble
  const aiWrapper = document.createElement('div');
  aiWrapper.className = 'chat-message-wrapper ai-side';
  aiWrapper.innerHTML = `
    <div class="avatar"><img src="/static/xiscoB.png"></div>
    <div class="message ai-msg">
      
    </div>
  `;
  messageList.appendChild(aiWrapper);

  try {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text })
    });

    if (!response.ok) throw new Error(`Server error ${response.status}`);

	const aiMessageDiv = aiWrapper.querySelector('.ai-msg');
	aiMessageDiv.innerHTML = ""; // remove typing dots

	const reader = response.body.getReader();
	const decoder = new TextDecoder();

	let fullText = "";

	while (true) {
		
		const { done, value } = await reader.read();
		if (done) break;

		const chunk = decoder.decode(value, { stream: true });
		fullText += chunk;

		const safeHTML = DOMPurify.sanitize(marked.parse(fullText));
		aiMessageDiv.innerHTML = safeHTML;

		// scroll at bottom
		window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
	}

	lastAiResponse = fullText;
	saveChatState();

	if (isVoiceEnabled) {
		speakText(lastAiResponse);
	}
    

	// Add per-message speaker button
	const speakBtn = document.createElement("button");
	speakBtn.type = "button";
	speakBtn.className = "msg-tts-btn";
	speakBtn.title = "Read aloud";
	speakBtn.innerHTML = `<i class="fa fa-volume-mute"></i>`;

	// store clean text for speech directly on the button
	speakBtn.dataset.speech = stripLinksForSpeech(fullText);

	aiMessageDiv.appendChild(speakBtn);


    // wrap tables
    aiMessageDiv.querySelectorAll('table').forEach(table => {
      if (table.parentElement?.classList.contains('table-scroll')) return;
      const wrapper = document.createElement('div');
      wrapper.className = 'table-scroll';
      table.parentNode.insertBefore(wrapper, table);
      wrapper.appendChild(table);
    });

    // highlight code
    aiMessageDiv.querySelectorAll('pre code').forEach(block => {
      hljs.highlightElement(block);
    });

  } catch (err) {
    aiWrapper.querySelector('.ai-msg').textContent =
      "Sorry — something went wrong. Please try again.";
    console.error(err);
  }

  window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
}

// Helper function to toggle the text
function toggleMessage(button) {
    const textDiv = button.previousElementSibling;
    const isCollapsed = textDiv.classList.contains('collapsed');

    if (isCollapsed) {
        textDiv.classList.remove('collapsed');
        textDiv.style.maskImage = 'none'; 
        textDiv.style.webkitMaskImage = 'none';
        button.innerHTML = 'Show less <i class="fa fa-angle-up"></i>';
    } else {
        textDiv.classList.add('collapsed');
        textDiv.style.maskImage = 'linear-gradient(180deg, black 50%, transparent 100%)';
        textDiv.style.webkitMaskImage = 'linear-gradient(180deg, black 50%, transparent 100%)';
        button.innerHTML = 'Expand text <i class="fa fa-angle-down"></i>';
    }
}


// Attach to Button
sendBtn.addEventListener('click', sendMessage);

// Attach to Enter Key
chatInput.addEventListener('keydown', (e) => {
  const isMobile = window.innerWidth < 768;

  if (!isMobile && e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

// TypeWriter
const textElement = document.getElementById("typewriter");
const phrases = [
    "I speak english?",      // English
    "Je parle français",   // French
    "Yo hablo español"       // Spanish
];

let phraseIndex = 0;
let charIndex = 0;
let isDeleting = false;
let typeSpeed = 100;

function type() {
    const currentPhrase = phrases[phraseIndex];
    
    if (isDeleting) {
        // Remove characters
        textElement.textContent = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
        typeSpeed = 50; // Deleting is usually faster
    } else {
        // Add characters
        textElement.textContent = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
        typeSpeed = 100;
    }

    // Logic for switching between typing and deleting
    if (!isDeleting && charIndex === currentPhrase.length) {
        // Pause at the end of the phrase
        isDeleting = true;
        typeSpeed = 2000; // Wait 2 seconds before deleting
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        typeSpeed = 500; // Wait a bit before starting next phrase
    }

    setTimeout(type, typeSpeed);
}



// Start the animation when the page loads
document.addEventListener("DOMContentLoaded", () => {
    if (textElement) type();
});



// detect voice language
function detectLang(text) {
  const t = (text || "").toLowerCase();
  // Checks for French-specific accents and common functional words (le, la, est, etc.)
  const isFrench = 
    /[àâçéèêëîïôùûüÿœæ]/i.test(t) || 
    /\b(le|la|les|un|une|est|et|que|qui|dans|pas|ce|ca|ça|pour|en|bonjour|merci)\b/i.test(t);
  
  if (isFrench) return "fr-FR";

  // Checks for Spanish-specific characters (ñ, ¿, ¡) and common functional words
  const isSpanish = 
    /[ñáéíóúü¿¡]/i.test(t) || 
    /\b(el|la|los|las|hola|gracias|por|para|con|que|si|no)\b/i.test(t);
  
  if (isSpanish) return "es-ES";

  // Default Fallback
  return "en-US";
}

// male voice selection
function findVoiceForLang(lang, voices) {
  const L2 = (lang || "").slice(0, 2).toLowerCase();

  const qualityHints = ["neural", "natural", "premium", "enhanced", "google"];
  const maleNameHints = ["daniel", "alex", "fred", "jorge", "diego", "carlos", "thomas", "henri", "paul", "arnaud"];

  const byLang = v =>
    ((v.lang || "").toLowerCase().startsWith(L2));

  const isQuality = v =>
    qualityHints.some(h =>
      ((v.name || "").toLowerCase().includes(h))
    );

  const isMaleish = v =>
    maleNameHints.some(h =>
      ((v.name || "").toLowerCase().includes(h))
    );

  // 1️⃣ language + quality + male
  let v = voices.find(v => byLang(v) && isQuality(v) && isMaleish(v));
  if (v) return v;

  // 2️⃣ language + quality
  v = voices.find(v => byLang(v) && isQuality(v));
  if (v) return v;

  // 3️⃣ language + male
  v = voices.find(v => byLang(v) && isMaleish(v));
  if (v) return v;

  // 4️⃣ language only
  v = voices.find(byLang);
  if (v) return v;

  return voices[0] || null;
}

// voice
let ttsUnlocked = false;
let currentUtterance = null;
let currentBtn = null;

function unlockTTSOnce() {
  if (ttsUnlocked) return;
  ttsUnlocked = true;

  try {
    speechSynthesis.cancel();
    speechSynthesis.resume();
    const u = new SpeechSynthesisUtterance(" ");
    u.volume = 0;
    speechSynthesis.speak(u);
  } catch (e) {
    console.warn("TTS unlock failed:", e);
  }
}

let isVoiceEnabled = false;
let VOICES = [];

function loadVoices() {
  VOICES = window.speechSynthesis.getVoices() || [];
  return VOICES;
}

window.speechSynthesis.onvoiceschanged = () => {
  loadVoices();
  console.log("Voices loaded:", VOICES.length);
};




function setupVoice() {
  const voiceToggle = document.getElementById("voiceToggle");
  const voiceIcon = document.getElementById("voiceIcon");
  if (!voiceToggle || !voiceIcon) return;

  if (voiceToggle.dataset.bound === "1") return;
  voiceToggle.dataset.bound = "1";

  // warm up voices
  loadVoices();

  voiceToggle.addEventListener("click", (e) => {
    e.preventDefault();
    e.stopPropagation();

    isVoiceEnabled = !isVoiceEnabled;

    if (isVoiceEnabled) {
      unlockTTSOnce();         // ✅ must happen from user click
      speechSynthesis.resume(); // ✅ unpause engine

      voiceIcon.className = "fa fa-volume-up";
      voiceIcon.style.color = "#2e0074";

      if (lastAiResponse) speakText(lastAiResponse);
    } else {
      voiceIcon.className = "fa fa-volume-mute";
      voiceIcon.style.color = "black";
      speechSynthesis.cancel();
    }

    console.log("Voice enabled:", isVoiceEnabled, "voices:", (speechSynthesis.getVoices() || []).length);
  });
}

document.addEventListener("DOMContentLoaded", setupVoice);


function speakText(text, { onStart, onEnd, onError } = {}) {
  const cleanText = stripLinksForSpeech(text || "");
  if (!cleanText.trim()) return;

  speechSynthesis.cancel();
  speechSynthesis.resume();

  const lang = detectLang(cleanText);

  function actuallySpeak() {
    const voices = speechSynthesis.getVoices() || [];
    const selectedVoice = findVoiceForLang(lang, voices);

    const u = new SpeechSynthesisUtterance(cleanText);
    u.lang = lang;

    if (selectedVoice) {
      u.voice = selectedVoice;
    }

    u.onstart = () => onStart && onStart(selectedVoice, lang);
    u.onend = () => onEnd && onEnd();
    u.onerror = (e) => onError && onError(e);

    setTimeout(() => speechSynthesis.speak(u), 100);
  }

  // 🔹 THIS IS FIX 2
  const voicesNow = speechSynthesis.getVoices() || [];

  if (!voicesNow.length) {
    speechSynthesis.onvoiceschanged = () => {
      speechSynthesis.onvoiceschanged = null;
      actuallySpeak();
    };
    return;
  }

  actuallySpeak();
}

// url stripping
function stripLinksForSpeech(text) {
  if (!text) return "";

  return text
    // LinkedIn ONLY → "Name on LinkedIn"
    .replace(
      /\[([^\]]+)\]\((https?:\/\/(www\.)?linkedin\.com[^\)]*)\)/gi,
      "$1"
    )

    // Any other markdown link → just the text
    .replace(
      /\[([^\]]+)\]\((https?:\/\/[^\)]+)\)/g,
      "$1"
    )

    // Raw URLs
    .replace(/https?:\/\/\S+/g, "")
    .replace(/www\.\S+/g, "")

    // Clean spacing
    .replace(/\s{2,}/g, " ")
    .trim();
}

// Working fine and sound is ok on histroy

(function () {
  const INACTIVITY_LIMIT = 5 * 60 * 1000;   // 2 mins
  const WARNING_AT = 4 * 60 * 1000;       // 1.5 mins

  let lockTimer = null;
  let warnTimer = null;
  let pausedUntil = 0;

  function clearTimers() {
    if (lockTimer) clearTimeout(lockTimer);
    if (warnTimer) clearTimeout(warnTimer);
    lockTimer = null;
    warnTimer = null;
  }

  function scheduleTimers() {
    clearTimers();

    const now = Date.now();
    const pauseRemaining = Math.max(0, pausedUntil - now);

    warnTimer = setTimeout(() => {
      showInactivityWarning();
    }, pauseRemaining + WARNING_AT);

    lockTimer = setTimeout(() => {
		saveChatState();
      window.location.href = "/lock";
    }, pauseRemaining + INACTIVITY_LIMIT);
  }

  function resetTimer() {
    scheduleTimers();
  }

  // ✅ Global pause you can call from anywhere
  window.pauseAutoLock = function (ms = 40000) {
    pausedUntil = Date.now() + ms;
    scheduleTimers();
  };

  ["mousemove","mousedown","keydown","scroll","touchstart","click"]
    .forEach(evt => document.addEventListener(evt, resetTimer, { passive: true }));

  resetTimer();
})();

function pauseAutoLock() {
  window.dispatchEvent(new Event("pauseAutoLock")); 

  clearTimeout(window._pauseLockTimer);
  window._pauseLockTimer = setTimeout(() => {
    window.dispatchEvent(new Event("resumeAutoLock"));
  }, 30000);
}

function showInactivityWarning() {
  if (document.getElementById("lock-warning")) return;

  const div = document.createElement("div");
  div.id = "lock-warning";
  div.textContent = "Chat session will be locked soon due to inactivity.";
  div.style.cssText = `
    position: fixed;
    bottom: 80px;
    left: 50%;
    transform: translateX(-50%);
    background: #111;
    color: #fff;
    padding: 10px 16px;
    border-radius: 6px;
    z-index: 9999;
    font-size: 14px;
	white-space: nowrap;     
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    pointer-events: none;
  `;

  document.body.appendChild(div);

  setTimeout(() => div.remove(), 10000);
}


// resume chat
const CHAT_STORAGE_KEY = "xisco_chat_state_v1";

function saveChatState() {
  const messageList = document.getElementById("messageList");
  const welcomeSection = document.getElementById("welcomeSection");
  const chatMessages = document.getElementById("chatMessages");
  const inputWrapper = document.getElementById("inputWrapper");

  if (!messageList) return;

  const state = {
    html: messageList.innerHTML, // save bubbles exactly
    isWelcomeHidden: welcomeSection ? (getComputedStyle(welcomeSection).display === "none") : true,
    isChatVisible: chatMessages ? (getComputedStyle(chatMessages).display !== "none") : true,
    inputMode: inputWrapper ? (inputWrapper.classList.contains("chatting-mode") ? "chatting" : "initial") : "chatting",
    lastAiResponse: window.lastAiResponse || "",
    savedAt: Date.now()
  };

  localStorage.setItem(CHAT_STORAGE_KEY, JSON.stringify(state));
}

function restoreChatState() {
  const raw = localStorage.getItem(CHAT_STORAGE_KEY);
  if (!raw) return;

  const state = JSON.parse(raw);

  const messageList = document.getElementById("messageList");
  const welcomeSection = document.getElementById("welcomeSection");
  const chatMessages = document.getElementById("chatMessages");
  const inputWrapper = document.getElementById("inputWrapper");

  if (!messageList) return;

  // restore messages
  messageList.innerHTML = state.html || "";

  // restore UI mode
	if (welcomeSection) welcomeSection.style.display = state.isWelcomeHidden ? "none" : "";
	if (chatMessages)   chatMessages.style.display   = state.isChatVisible   ? ""     : "none";

	if (welcomeSection && getComputedStyle(welcomeSection).display !== "none") {
		document.body.classList.remove("chatting-mode-active");
	}

  if (inputWrapper) {
    inputWrapper.classList.remove("initial-state", "chatting-mode");
    inputWrapper.classList.add(state.inputMode === "chatting" ? "chatting-mode" : "initial-state");
  }

  window.lastAiResponse = state.lastAiResponse || "";

  // re-apply table wrapping + highlight for restored HTML
  messageList.querySelectorAll(".ai-msg table").forEach(table => {
    if (table.parentElement?.classList.contains("table-scroll")) return;
    const wrapper = document.createElement("div");
    wrapper.className = "table-scroll";
    table.parentNode.insertBefore(wrapper, table);
    wrapper.appendChild(table);
  });

  messageList.querySelectorAll(".ai-msg pre code").forEach(block => {
    hljs.highlightElement(block);
  });

  // scroll to bottom
  window.scrollTo({ top: document.body.scrollHeight, behavior: "auto" });
}
document.addEventListener("DOMContentLoaded", restoreChatState);


function clearChatState() {
  localStorage.removeItem(CHAT_STORAGE_KEY);
  if (window.speechSynthesis) window.speechSynthesis.cancel();
  location.reload();
}

document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("newChatBtn");
  if (!btn) return;

  btn.addEventListener("click", () => {
    // optional confirm
    if (confirm("Start a new chat? This will clear the current chat history on this device.")) {
      clearChatState();
    }
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const list = document.getElementById("messageList");
  if (!list) return;

  list.addEventListener("click", (e) => {
    const btn = e.target.closest(".msg-tts-btn");
    if (!btn) return;

    e.preventDefault();
    e.stopPropagation();

    // Unlock audio engine from a user click (Safari/Chrome requirement)
    unlockTTSOnce();
    speechSynthesis.resume();

    // If this same button is currently speaking -> stop
    if (currentBtn === btn && speechSynthesis.speaking) {
      speechSynthesis.cancel();
      btn.innerHTML = `<i class="fa fa-volume-mute"></i>`;
      currentBtn = null;
      return;
    }

    // If another message is speaking -> stop it + reset icon
    if (currentBtn && currentBtn !== btn) {
      currentBtn.innerHTML = `<i class="fa fa-volume-mute"></i>`;
      speechSynthesis.cancel();
    }

    const speechText = btn.dataset.speech || btn.closest(".ai-msg")?.innerText || "";
    currentBtn = btn;

    // button shows ⏹ while speaking
    speakText(speechText, {
      onStart: () => btn.innerHTML = "⏹",
      onEnd: () => {
        if (currentBtn === btn) currentBtn = null;
        btn.innerHTML = `<i class="fa fa-volume-mute"></i>`;
      },
      onError: () => {
        if (currentBtn === btn) currentBtn = null;
        btn.innerHTML = `<i class="fa fa-volume-mute"></i>`;
      }
    });
  });
});
