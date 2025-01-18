describe('Error Handling', () => {
  beforeEach(() => {
    cy.visit('/some-non-existent-page');
  });

  it('should show a 404 error page', () => {
    cy.contains('Page not found').should('be.visible');
    cy.url().should('include', '/404');
  });
});

