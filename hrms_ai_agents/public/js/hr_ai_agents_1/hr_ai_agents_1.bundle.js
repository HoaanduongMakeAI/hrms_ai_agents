import { createApp } from "vue";
import App from "./App.vue";


class HrAiAgents1 {
	constructor({ page, wrapper }) {
		this.$wrapper = $(wrapper);
		this.page = page;

		this.init();
	}

	init() {
		this.setup_page_actions();
		this.setup_app();
	}

	setup_page_actions() {
		// setup page actions
		this.primary_btn = this.page.set_primary_action(__("Print Message"), () =>
	  frappe.msgprint("Hello My Page!")
		);
	}

	setup_app() {
		// create a vue instance
		let app = createApp(App);
		// mount the app
		this.$hr_ai_agents_1 = app.mount(this.$wrapper.get(0));
	}
}

frappe.provide("frappe.ui");
frappe.ui.HrAiAgents1 = HrAiAgents1;
export default HrAiAgents1;