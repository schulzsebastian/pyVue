var colorTest = Vue.extend({
  template: `
    <p style="color: red">I am a child</p>
  `
})

var boldTest =Vue.extend({
  props: {
    y: String
  },
  template: `
    <div><b>I am a parent</b></div><color-test></color-test><div v-text="y"></div>
  `,
  components:{
    'color-test': colorTest
  }
})

Vue.component('elo', {
  props: {
    x: String
  },
  template: `
    <bold-test :y="x"></bold-test>
  `,
  components: {
    'bold-test': boldTest
  }
})

var vm = new Vue({
  el: "#app",
  data: {
    test: 'test'
  }
})