import getFullResponseFromAPI from './1-promise';

describe('getFullResponseFromAPI', () => {
  it('should resolve with the correct data when success is true', async () => {
    const response = await getFullResponseFromAPI(true);
    expect(response).toEqual({
      status: 200,
      body: 'Success',
    });
  });

  it('should reject with an error when success is false', async () => {
    try {
      await getFullResponseFromAPI(false);
    } catch (error) {
      expect(error).toEqual(new Error('The fake API is not working currently'));
    }
  });
});
