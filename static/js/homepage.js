var homepageSection = Vue.extend({
  template: `
    <div class="section">
      <h1>SEBASTIAN SCHULZ</h1>
      <h5>Python & GIS Developer</h5>
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

var skillsList = Vue.extend({
  props: {
    lang: String,
    items: Array
  },
  template: `
    <table>
      <tbody>
        <tr v-for="item in items">
          <td class="col s6" v-text="item.name"></td>
          <td class="col s6"><div :id="lang+item.id"></div></td>
        </tr>
      </tbody>
    </table>
  `,
  ready: function(){
    var self = this;
    self.items.forEach(function(skill){
      var bar = new ProgressBar.Line('#'+self.lang+skill.id, {
        strokeWidth: 3,
        easing: 'easeInOut',
        duration: 5000,
        color: '#333',
        trailColor: '#eee',
        trailWidth: 1,
        svgStyle: {width: '100%', height: '50%'}
      })
      bar.animate(skill.level)
    })
  }
})

Vue.component('skills-section',{
  data: function(){
    return {
      python: pythonSkills,
      pythonPrefix: 'py',
      js: jsSkills,
      jsPrefix: 'js',
      db: dbSkills,
      dbPrefix: 'db',
      other: otherSkills,
      otherPrefix: 'other'
    }
  },
  template: `
  <div class="section">
    <div class="container">
      <div class="row">
        <div class="col s6">
          <h5>Python</h5><br>
          <skills-list :lang="pythonPrefix" :items="python"></skills-list>
        </div>
        <div class="col s6">
          <h5>Javascript</h5><br>
          <skills-list :lang="jsPrefix" :items="js"></skills-list>
        </div>
      </div>
      <div class="row">
        <div class="col s6">
          <h5>Databases</h5><br>
          <skills-list :lang="dbPrefix" :items="db"></skills-list>
        </div>
        <div class="col s6">
          <h5>Other</h5><br>
          <skills-list :lang="otherPrefix" :items="other"></skills-list>
        </div>
      </div>
    </div>
  </div>
  `,
  components: {
    'skills-list': skillsList
  }
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