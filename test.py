import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://gamedaytldr.live/');
  await page.locator('.promo-option-indicator-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9').first().click();
  await page.locator('.epl-optin-toggle-checkbox-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9').click();
  await page.locator('.promo-option-card-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9.is-radio > .promo-option-inner-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9 > .promo-option-indicator-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9').first().click();
  await page.getByLabel('Favourite EPL Team *').selectOption('Arsenal');
  await page.getByText('✉️ Email').click();
  await page.getByRole('textbox', { name: 'Email Address *' }).click();
  await page.getByRole('textbox', { name: 'Email Address *' }).fill('test@gmail.com');
  await page.getByRole('textbox', { name: 'Favourite Team *' }).click();
  await page.getByRole('textbox', { name: 'Favourite Team *' }).press('CapsLock');
  await page.getByRole('textbox', { name: 'Favourite Team *' }).fill('USA');
  await page.getByRole('textbox', { name: 'Favourite Team *' }).press('CapsLock');
  await page.getByRole('button', { name: 'Add to Cart' }).click();
});