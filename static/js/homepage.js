var homepageSection = Vue.extend({
  template: `
    <div class="section">
      <h1>SEBASTIAN SCHULZ</h1>
      <h5>Python & GIS Developer</h5>
    </div>
  `
})

var skillsSection = Vue.extend({
  template: `
    <div class="section">
      <h5>Skills</h5
    </div>
  `
})

var travelSection = Vue.extend({
  template: `
    <div class="section">
      <h5>I like to travel</h5>
    </div>
  `
})

var contactSection = Vue.extend({
  template: `
    <div class="section">
      <h5>Contact</h5>
    </div>
  `
})

Vue.component('fullpage-app', {
  template: `
    <div id="fullpage">
      <homepage-section></homepage-section>
      <skills-section></skills-section>
      <travel-section></travel-section>
      <contact-section></contact-section>
    </div>
  `,
  components: {
    'homepage-section': homepageSection,
    'skills-section': skillsSection,
    'travel-section': travelSection,
    'contact-section': contactSection
  },
  ready: function(){
    $(document).ready(function() {
      $('#fullpage').fullpage({
        navigation: true,
        navigationPosition: 'right',
        navigationTooltips: ['Homepage', 'Skills', 'Interests', 'Contact']
      });
    });
  }
})

var vm = new Vue({
  el: "#app"
})