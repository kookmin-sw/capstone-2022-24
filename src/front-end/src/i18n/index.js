import { createI18n } from 'vue-i18n';

import en from './locales/en.json';
import ko from './locales/ko.json';

export const i18n = createI18n({
	locale: 'ko', // set locale
	fallbackLocale: 'ko', // set fallback locale
	messages: { en, ko }, // set locale messages
});
