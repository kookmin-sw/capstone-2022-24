import { mount } from '@vue/test-utils';
import GNB from '@/components/GNB.vue';

describe('GNB', () => {
	const wrapper = mount(GNB, {
		computed: {
			isLogin: () => false,
			userProfile() {
				return { nickname: 'example-nickname' };
			},
		},
	});

	it('render logo img', () => {
		expect(wrapper.find('.logo-img').isVisible()).toBe(true);
	});
	it('render text menu', () => {
		const textMenu = wrapper.find('.text-menu-wrapper');
		const textMenuLink = textMenu.findAll('router-link');
		expect(textMenuLink[0].isVisible()).toBe(true);
		expect(textMenuLink[1].isVisible()).toBe(true);
		expect(textMenuLink[2].isVisible()).toBe(true);
	});
	it('render login button', () => {
		const btnWrapper = wrapper.find('.btn-wrapper');
		expect(btnWrapper.find('#login-btn').isVisible()).toBe(true);
	});
});
