// ActionScript file
package com.petetweet.client.events
{
	import flash.events.Event;

	public class RegisterPassEvent extends Event
	{
		public function RegisterPassEvent(bubbles:Boolean=false, cancelable:Boolean=false)
		{
			super("RegisterPassEvent", bubbles, cancelable);
		}
		
		override public function clone():Event {
			return new RegisterPassEvent();
		}
		
	}
}